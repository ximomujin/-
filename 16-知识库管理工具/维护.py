#!/usr/bin/env python3
"""从知识库根目录运行的本地维护工具。"""

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import date
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit, urlunsplit
from urllib.request import Request, urlopen


NAV = Path("00-学习导航")
LIBRARY = Path("12-教材与学习资源库")
TOPICS = NAV / "主题数据库.json"
PROGRESS = NAV / "学习进度.json"
RESOURCES = LIBRARY / "资源清单.json"
FAILURES = LIBRARY / "下载失败记录.json"
MODULE = Path("16-知识库管理工具")
LINK_REPORT = MODULE / "维护记录" / "链接核验.json"
MIB = 1024**2
SOFT_BUDGET = 1024 * MIB
USER_AGENT = "PersonalPhysicsLibrary/1.0 (public resource link check)"
URL_SECRET_FIELDS = re.compile(
    r"(^|&)(token|api[_-]?key|access[_-]?key|password|passwd|secret|signature|sig|x-amz-[^=]+)=",
    re.IGNORECASE,
)


def repo_path(root, relative):
    path = Path(relative)
    result = (root / path).resolve()
    if path.is_absolute() or not result.is_relative_to(root) or ".git" in path.parts:
        raise ValueError(f"需要仓库内非 Git 元数据的相对路径：{relative}")
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="\n", dir=path.parent, delete=False
    ) as temporary:
        temporary_path = Path(temporary.name)
        try:
            temporary.write(content)
            temporary.close()
            temporary_path.replace(path)
        finally:
            temporary_path.unlink(missing_ok=True)


def write_json(path, data):
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


@contextmanager
def exclusive_update(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(f".{path.name}.lock")
    try:
        lock.mkdir()
    except FileExistsError as error:
        raise ValueError(f"记录正在更新：{path.name}") from error
    try:
        yield
    finally:
        lock.rmdir()


def records(root, path, key):
    document = read_json(root / path)
    rows = document.get(key) if isinstance(document, dict) else None
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError(f"{path} 必须含对象数组 {key}")
    return rows


def display(value):
    if value is None or value == "":
        return "待核实"
    return " ".join(str(value).splitlines()).replace("|", "\\|")


def markdown_table(headers, rows):
    def line(row):
        return "| " + " | ".join(row) + " |"

    columns = [line(headers), line(["---"] * len(headers))]
    columns.extend(line(row) for row in rows)
    return "\n".join(columns)


def markdown_link(label, target):
    text = display(label).replace("[", "\\[").replace("]", "\\]")
    href = quote(str(target), safe="/:#?&=+@%~._-")
    return f"[{text}]({href})"


def relative_link(label, origin, target):
    return markdown_link(label, Path(os.path.relpath(target, origin.parent)).as_posix())


def stage_number(topic):
    stage = topic.get("stage")
    return stage if type(stage) is int and 1 <= stage <= 4 else math.inf


def topic_sort_key(topic):
    return (stage_number(topic), str(topic.get("name_zh") or ""), str(topic.get("id") or ""))


def stage_title(stage):
    return f"阶段 {stage}" if math.isfinite(stage) else "阶段待编排"


def topic_rows(root, topics, destination):
    for topic in topics:
        title = display(topic.get("name_zh"))
        directory = topic.get("directory")
        if directory:
            name = repo_path(root, directory) / "README.md"
            if name.is_file():
                title = relative_link(topic.get("name_zh"), destination, Path(directory) / "README.md")
        yield (
            title,
            display(topic.get("name_en")),
            stage_title(stage_number(topic)),
            display(subject(topic)),
        )


def subject(topic):
    directory = topic.get("directory")
    return Path(directory).parts[0] if directory else "待归类"


def generate_indexes(root, _args):
    topics = sorted(records(root, TOPICS, "courses"), key=topic_sort_key)
    headers = ("学习主题", "英文名称", "学习阶段", "学科模块")
    groups = (
        (Path("主题总索引.md"), "主题总索引", lambda _row: "主题", str),
        (NAV / "阶段索引.md", "阶段索引", stage_number, stage_title),
        (NAV / "学科索引.md", "学科索引", subject, str),
    )
    for destination, title, key, label in groups:
        grouped = defaultdict(list)
        for topic in topics:
            grouped[key(topic)].append(topic)
        source_link = relative_link("主题数据库", destination, TOPICS)
        parts = [f"# {title}", f"当前共 {len(topics)} 个学习主题。{source_link}"]
        if not grouped:
            parts.append("可在主题数据库录入学习主题后重新生成索引。")
        for group, rows in sorted(grouped.items()):
            table = markdown_table(headers, topic_rows(root, rows, destination))
            parts.append(f"## {label(group)}\n\n{table}")
        write_text(root / destination, "\n\n".join(parts) + "\n")
        print(destination)
    return 0


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(MIB), b""):
            digest.update(block)
    return digest.hexdigest()


def is_public_url(url):
    if not isinstance(url, str):
        return False
    try:
        parsed = urlsplit(url)
        return (
            parsed.scheme in {"http", "https"}
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
            and not URL_SECRET_FIELDS.search(parsed.query)
            and not any(character.isspace() for character in url)
        )
    except ValueError:
        return False


def validate_resources(root, _args):
    resources = records(root, RESOURCES, "resources")
    checked, errors, seen = 0, [], set()
    for resource in resources:
        resource_id = resource.get("id")
        if not isinstance(resource_id, str) or not resource_id or resource_id in seen:
            errors.append(f"资源编号为空、格式错误或重复：{resource_id}")
            continue
        seen.add(resource_id)
        path = resource.get("path")
        if not path:
            continue
        full_path = repo_path(root, path)
        if not full_path.is_file():
            errors.append(f"{resource_id} 的本地文件缺失：{path}")
            continue
        checked += 1
        errors.extend(f"{resource_id} {problem}" for problem in metadata_problems(resource))
        if resource.get("size_bytes") != full_path.stat().st_size:
            errors.append(f"{resource_id} 的文件大小与清单不一致")
        if str(resource.get("sha256", "")).lower() != sha256(full_path):
            errors.append(f"{resource_id} 的 SHA-256 与清单不一致")
    print(f"清单 {len(resources)} 条，检查本地资源 {checked} 份，发现 {len(errors)} 项问题。")
    for error in errors:
        print(error)
    return int(bool(errors))


def metadata_problems(resource):
    if not resource.get("license") or not is_public_url(resource.get("license_evidence_url")):
        yield "缺少许可证或公开的授权证据链接"
    if not all(is_public_url(resource.get(field)) for field in ("download_url", "official_url")):
        yield "缺少公开的原始下载链接或官方来源"


def update_archive(root, args):
    manifest = root / RESOURCES
    with exclusive_update(manifest):
        document = read_json(manifest)
        resources = document.get("resources") if isinstance(document, dict) else None
        if not isinstance(resources, list) or not all(isinstance(row, dict) for row in resources):
            raise ValueError(f"{RESOURCES} 必须含对象数组 resources")
        matched = [row for row in resources if row.get("id") == args.id]
        if len(matched) != 1:
            raise ValueError(f"需要唯一的资源编号：{args.id}")
        resource = matched[0]
        problems = list(metadata_problems(resource))
        if problems:
            raise ValueError("，".join(problems))
        file = repo_path(root, args.file)
        if not file.is_file():
            raise ValueError(f"找不到存档文件：{args.file}")
        relative = file.relative_to(root).as_posix()
        digest = sha256(file)
        for other in resources:
            if other is not resource and other.get("path") and other.get("sha256") == digest:
                raise ValueError(f"已存档相同文件：{other['path']}，请沿用资源编号 {other['id']}")
        if file.suffix.lower() == ".pdf":
            renderer = shutil.which("pdftoppm")
            if renderer is None:
                raise ValueError("登记 PDF 前需要安装 Poppler 的 pdftoppm")
            problem = pdf_structure(file, renderer)
            if problem:
                raise ValueError(f"PDF 检查失败：{problem}")
        resource.update(path=relative, size_bytes=file.stat().st_size, sha256=digest,
                        verified_date=date.today().isoformat())
        write_json(manifest, document)
    print(f"{args.id}\t{relative}\t{digest}")
    return 0


def generate_manifest(root, _args):
    resources = records(root, RESOURCES, "resources")
    destination = LIBRARY / "资源核验索引.md"
    headers = ("编号", "资源", "类型", "语言", "许可证", "存档", "核验日期")
    rows = []
    for resource in resources:
        title = display(resource.get("title"))
        official_url = resource.get("official_url")
        if is_public_url(official_url):
            title = markdown_link(resource.get("title"), official_url)
        path = resource.get("path")
        local = relative_link("本地文件", destination, path) if path else "链接"
        rows.append(
            (display(resource.get("id")), title, display(resource.get("type")),
             display(resource.get("language")), display(resource.get("license")), local,
             display(resource.get("verified_date")))
        )
    description = "授权证据、下载链接、大小和校验值见 [资源清单.json](资源清单.json)。"
    table = markdown_table(headers, rows)
    write_text(root / destination, f"# 资源核验索引\n\n共 {len(resources)} 条记录。{description}\n\n{table}\n")
    print(destination)
    return validate_resources(root, _args)


def git_result(root, *arguments):
    return subprocess.run(["git", "-C", str(root), *arguments], capture_output=True, check=False)


def repository_files(root):
    result = git_result(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z")
    if result.returncode == 0:
        paths = set(result.stdout.decode("utf-8", errors="surrogateescape").strip("\0").split("\0"))
        candidates = (root / path for path in sorted(paths) if path)
    else:
        candidates = (file for file in root.rglob("*") if ".git" not in file.relative_to(root).parts)
    return sorted(path for path in candidates if not path.is_symlink() and path.is_file())


def duplicate_groups(paths):
    by_size = defaultdict(list)
    for path in paths:
        by_size[path.stat().st_size].append(path)
    for same_size in by_size.values():
        if len(same_size) < 2:
            continue
        by_hash = defaultdict(list)
        for path in same_size:
            by_hash[sha256(path)].append(path)
        yield from ((digest, group) for digest, group in by_hash.items() if len(group) > 1)


def detect_references(root, retiring):
    relative = retiring.relative_to(root).as_posix()
    forms = {relative, retiring.name, quote(relative), quote(retiring.name)}
    for path in repository_files(root):
        if path == retiring or path.suffix.lower() not in {".md", ".json", ".csv", ".txt", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if any(form in text for form in forms):
            yield path.relative_to(root)


def deduplicate(root, args):
    if args.delete and args.keep:
        retiring = repo_path(root, args.delete)
        keeper = repo_path(root, args.keep)
        if (root / args.delete).absolute() != retiring or (root / args.keep).absolute() != keeper:
            raise ValueError("应用去重时请使用规范仓库相对路径，避免符号链接")
        if not retiring.is_file() or not keeper.is_file() or retiring == keeper:
            raise ValueError("需要两个不同的现有文件")
        if retiring.stat().st_size != keeper.stat().st_size or sha256(retiring) != sha256(keeper):
            raise ValueError("大小或 SHA-256 不同，无法判定为重复文件")
        references = list(detect_references(root, retiring))
        if references:
            raise ValueError("需要先更新可能引用该文件的记录：" + "、".join(map(str, references)))
        retiring.unlink()
        print(f"已删除 {args.delete}，保留 {args.keep}。")
        return 0
    if args.delete or args.keep:
        raise ValueError("应用去重时需同时指定 --删除 和 --保留")
    groups = list(duplicate_groups(repository_files(root)))
    for digest, group in groups:
        print(digest)
        for path in group:
            print(f"  {path.relative_to(root)}")
    print(f"发现 {len(groups)} 组完全相同的文件。")
    return 0


def pdf_structure(path, renderer):
    with path.open("rb") as stream:
        header = stream.read(1024)
        stream.seek(max(0, path.stat().st_size - 4096))
        tail = stream.read()
    if b"%PDF-" not in header or b"%%EOF" not in tail:
        return "缺少 PDF 文件头或结束标记"
    if renderer:
        result = subprocess.run([renderer, "-r", "12", str(path)], stdout=subprocess.DEVNULL,
                                stderr=subprocess.PIPE, timeout=120, check=False)
        diagnostics = result.stderr.decode(errors="replace").strip()
        if result.returncode or re.search(r"\b(?:syntax|internal|command line|i/o) error\b", diagnostics, re.I):
            return diagnostics.splitlines()[0] if diagnostics else f"页面解码退出码 {result.returncode}"
    return None


def validate_pdfs(root, args):
    paths = [repo_path(root, relative) for relative in args.files]
    if not paths:
        paths = [path for path in repository_files(root) if path.suffix.lower() == ".pdf"]
    renderer = shutil.which("pdftoppm")
    errors = 0
    for path in paths:
        try:
            problem = pdf_structure(path, renderer)
        except (OSError, subprocess.TimeoutExpired) as error:
            problem = str(error)
        errors += bool(problem)
        print(f"{path.relative_to(root)}\t{problem or '通过'}")
    print(f"检查 {len(paths)} 份 PDF，发现 {errors} 项问题。")
    if paths and renderer is None:
        print("安装 Poppler 的 pdftoppm 可继续验证每页是否可解码。")
    return 1 if errors else 2 if paths and renderer is None else 0


def log_failure(root, args):
    path = root / FAILURES
    if not is_public_url(args.url):
        raise ValueError("请填写不含凭据的公开下载链接")
    with exclusive_update(path):
        document = read_json(path) if path.exists() else {"failures": []}
        if not isinstance(document, dict) or not isinstance(document.get("failures"), list):
            raise ValueError(f"{FAILURES} 必须含对象数组 failures")
        document["failures"].append(
            {"id": args.id, "url": args.url, "attempted_date": date.today().isoformat(),
             "reason": args.reason, "retry_result": args.retry_result}
        )
        write_json(path, document)
    print(FAILURES)
    return 0


def public_urls(document):
    if isinstance(document, dict):
        for child in document.values():
            yield from public_urls(child)
    elif isinstance(document, list):
        for child in document:
            yield from public_urls(child)
    elif is_public_url(document):
        parsed = urlsplit(document)
        yield urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, ""))


def check_link(url, timeout):
    status = None
    for method in ("HEAD", "GET"):
        headers = {"User-Agent": USER_AGENT}
        if method == "GET":
            headers["Range"] = "bytes=0-4095"
        request = Request(url, headers=headers, method=method)
        try:
            with urlopen(request, timeout=timeout) as response:
                return {"url": url, "status": "有效", "http": response.status}
        except HTTPError as error:
            status = error.code
            error.close()
        except (URLError, OSError, TimeoutError, ValueError):
            continue
    return {"url": url, "status": "失效" if status in {404, 410} else "待核实", "http": status}


def check_links(root, args):
    paths = args.inputs or [RESOURCES]
    urls = sorted(set().union(*(set(public_urls(read_json(repo_path(root, path)))) for path in paths)))
    if args.timeout <= 0 or not 1 <= args.workers <= 16:
        raise ValueError("超时秒数须大于 0，并发数须在 1 至 16 之间")
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = list(executor.map(lambda url: check_link(url, args.timeout), urls))
    counts = {status: sum(row["status"] == status for row in results) for status in ("有效", "失效", "待核实")}
    for row in results:
        if row["status"] != "有效":
            print(f"{row['status']}\t{row['http'] or '无响应'}\t{row['url']}")
    print("链接核验 " + "，".join(f"{status} {number}" for status, number in counts.items()) + "。")
    if args.write:
        write_json(root / LINK_REPORT, {"date": date.today().isoformat(), "counts": counts, "results": results})
        print(LINK_REPORT)
    return int(bool(counts["失效"]))


def progress_summary(root, args):
    topics = records(root, TOPICS, "courses")
    progress = records(root, PROGRESS, "entries")
    by_id = {}
    for entry in progress:
        topic_id, percent = entry.get("topic_id"), entry.get("percent")
        if not isinstance(topic_id, str) or not topic_id or topic_id in by_id:
            raise ValueError(f"学习进度含重复或无效的主题标识：{topic_id}")
        if not isinstance(percent, (int, float)) or isinstance(percent, bool) or not 0 <= percent <= 100:
            raise ValueError(f"{topic_id} 的进度必须是 0 到 100 的数字")
        by_id[topic_id] = entry
    known_ids = {topic.get("id") for topic in topics if topic.get("id")}
    unknown = sorted(by_id.keys() - known_ids)
    if unknown:
        raise ValueError("进度记录引用主题数据库中不存在的标识：" + "、".join(unknown))
    rows, values = [], []
    for topic in sorted(topics, key=topic_sort_key):
        entry = by_id.get(topic.get("id"), {})
        percent = entry.get("percent", 0)
        status = entry.get("status") or ("已完成" if percent == 100 else "进行中" if percent else "未开始")
        rows.append((display(topic.get("name_zh")), stage_title(stage_number(topic)),
                     display(status), f"{percent:g}%"))
        values.append(percent)
    completed = values.count(100)
    active = sum(0 < percent < 100 for percent in values)
    average = sum(values) / len(values) if values else 0
    source_link = relative_link("进度数据", Path("学习进度.md"), PROGRESS)
    description = f"主题 {len(values)} 个，已完成 {completed} 个，进行中 {active} 个，平均进度 {average:.1f}%。{source_link}"
    table = markdown_table(("学习主题", "学习阶段", "状态", "进度"), rows)
    output = f"# 学习进度\n\n{description}\n\n{table}\n"
    if args.write:
        write_text(root / "学习进度.md", output)
        print("学习进度.md")
    print(description)
    return 0


def repository_size(root, _args):
    files = repository_files(root)
    sizes = {file: file.stat().st_size for file in files}
    worktree_bytes = sum(sizes.values())
    git_directory = git_result(root, "rev-parse", "--path-format=absolute", "--git-common-dir")
    git_bytes = 0
    if git_directory.returncode == 0:
        git_path = Path(git_directory.stdout.decode().strip())
        git_bytes = sum(path.stat().st_size for path in git_path.rglob("*")
                        if not path.is_symlink() and path.is_file())
    print(f"工作树 {worktree_bytes:,} 字节，Git 元数据 {git_bytes:,} 字节，合计 {(worktree_bytes + git_bytes):,} 字节。")
    if git_directory.returncode == 0:
        result = git_result(root, "count-objects", "-vH")
        if result.returncode == 0:
            print(result.stdout.decode().strip())
    for file, size in sorted(sizes.items(), key=lambda entry: entry[1], reverse=True)[:5]:
        print(f"{size / MIB:.2f} MiB\t{file.relative_to(root)}")
    exceeded = worktree_bytes + git_bytes > SOFT_BUDGET
    if exceeded:
        print("超过 1 GiB 软预算。可保留官方资源链接，并将可再下载的大文件移出仓库。")
    return int(exceeded)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--根目录", dest="root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)

    def command(name, help_text, function):
        subparser = commands.add_parser(name, help=help_text)
        subparser.set_defaults(function=function)
        return subparser

    command("生成索引", "生成主题总索引、阶段索引和学科索引", generate_indexes)
    command("生成清单", "生成资源核验索引并验证本地存档", generate_manifest)
    command("核验资源", "检查本地资源的大小、SHA-256 和授权证据字段", validate_resources)
    archive = command("更新存档校验", "为已核实授权的本地资源登记文件校验信息", update_archive)
    archive.add_argument("id", help="资源编号")
    archive.add_argument("file", help="存档文件的仓库相对路径")

    duplicates = command("文件去重", "查找按 SHA-256 判定完全相同的文件", deduplicate)
    duplicates.add_argument("--删除", dest="delete", help="指定要删除的重复文件，使用仓库相对路径")
    duplicates.add_argument("--保留", dest="keep", help="指定要保留的重复文件，使用仓库相对路径")

    pdfs = command("检查PDF", "检查文件边界及逐页解码", validate_pdfs)
    pdfs.add_argument("files", nargs="*", help="可选的仓库相对路径，默认检查全部 PDF")

    failure = command("记录下载失败", "追加下载失败或重试结果", log_failure)
    failure.add_argument("id", help="资源编号")
    failure.add_argument("url", help="公开下载链接")
    failure.add_argument("reason", help="具体失败原因")
    failure.add_argument("--重试结果", dest="retry_result", default="待重试")

    links = command("检查链接", "检查 JSON 清单中的公开链接", check_links)
    links.add_argument("inputs", nargs="*", help="可选的 JSON 文件仓库相对路径，默认检查资源清单")
    links.add_argument("--超时", dest="timeout", type=float, default=10)
    links.add_argument("--并发", dest="workers", type=int, default=6)
    links.add_argument("--写入", dest="write", action="store_true")

    progress = command("统计进度", "根据主题数据库和进度数据汇总学习进度", progress_summary)
    progress.add_argument("--写入", dest="write", action="store_true")

    command("检查容量", "统计文件与 Git 存储空间并检查 1 GiB 软预算", repository_size)
    args = parser.parse_args()
    try:
        return args.function(args.root.resolve(), args)
    except (OSError, TypeError, ValueError, subprocess.TimeoutExpired) as error:
        parser.exit(2, f"维护失败：{error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
