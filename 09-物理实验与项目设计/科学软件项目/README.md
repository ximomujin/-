# 科学软件项目

Scientific Software Project · 学习阶段 3

用一组测量值实现可独立测试的估计量，再提供带错误反馈的文件接口。

## 前置知识

[C 语言程序设计](../../08-%E7%BC%96%E7%A8%8B%E4%B8%8E%E8%AE%A1%E7%AE%97%E7%89%A9%E7%90%86/C%20%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/README.md)

## 章节知识树

1. 软件需求和输入输出
2. 数据表示
3. 算法与实现
4. 测试、性能和发布
5. 报告与维护

## 公式与推导

若同一物理量的独立测量值为 $x_i$，标准不确定度为 $\sigma_i$，则用 $w_i=\sigma_i^{-2}$ 加权。期望均值为 $\sum_i w_ix_i/\sum_i w_i$，标准不确定度为 $(\sum_i w_i)^{-1/2}$。

## 例题

两次独立测量分别为 $1.0\pm0.1$、$1.4\pm0.2$，逆方差加权结果为 $1.08\pm0.089$，写入自动验收样例。

## 习题

为一个计算结果同时准备手算样例、边界样例和错误数据，记录输出是否与预期相符。

## 应用、实验与验证

包含安装、运行及版本记录。

## 推导与案例

用逆方差加权平均构建边界样例和软件验收。 [推导、案例与练习](推导与案例.md)

## 教材索引

### 教材

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [Python 教程](https://docs.python.org/zh-cn/3/tutorial/) | 中文 · Python 3 官方在线文档 · 本科 | 数据结构、函数、模块、文件和异常 | 在线入口 |
| [Hello 算法](https://www.hello-algo.com/) | 中文 · 1.3.0 简体中文 Python 版 · 本科 | 数组与链表、栈与队列、树、哈希、图和复杂度；配合简体中文 Python 版复现书中案例 | [离线 PDF](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E7%AE%97%E6%B3%95%E5%85%A5%E9%97%A8-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88.pdf) |

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [12.010 Computational Methods of Scientific Programming](https://ocw.mit.edu/courses/12-010-computational-methods-of-scientific-programming-fall-2024/) | 英文 · fall 2024 · 本科 | Python、科学程序设计、数值方法与实践 | 在线入口 |
| [6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/) | 英文 · spring 2015 · 本科 | 算法复杂度、图、分治和动态规划 | 在线入口 |

### 习题

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [6.046J Design and Analysis of Algorithms: Assignments](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/assignments/) | 英文 · spring 2015 · 本科 | 复杂度、分治、动态规划和图算法 | 在线入口 |
| [Think Python 课程练习](https://allendowney.github.io/ThinkPython/) | 英文 · 第三版 · 本科 | 使用各章末 Exercises 或 Case Study；先写最小测试，再尝试不同输入验证 | 在线入口 |

### 在线资料

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [SciPy User Guide](https://docs.scipy.org/doc/scipy/tutorial/) | 英文 · 本科 | 线性代数、优化、积分、插值、统计和信号 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- [参考资料 2](https://docs.python.org/zh-cn/3/tutorial/index.html)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。合上笔记复述知识树，并独立完成本页练习。
- 拓展。将练习结果推广到一种新的条件，记录适用范围。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
