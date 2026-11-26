# 电子电路设计项目

Electronic Circuit Design Project · 学习阶段 2

从电路指标出发，用解析估算、仿真和测量交叉验证。

## 前置知识

[电路分析基础](../../06-%E7%94%B5%E8%B7%AF%E4%B8%8E%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF/%E7%94%B5%E8%B7%AF%E5%88%86%E6%9E%90%E5%9F%BA%E7%A1%80/README.md)、[模拟电子技术](../../06-%E7%94%B5%E8%B7%AF%E4%B8%8E%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF/%E6%A8%A1%E6%8B%9F%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF/README.md)

## 章节知识树

1. 规格与约束
2. 电路方案与器件选型
3. 仿真及样机
4. 测量和故障排查
5. 设计报告

## 公式与推导

串联 RC 电路从电容端取输出，复阻抗分压得 $H(j\omega)=1/(1+j\omega RC)$。使增益模降至直流值的 $1/\sqrt2$ 时有 $\omega_c RC=1$，故 $f_c=1/(2\pi RC)$。

## 例题

$R=10\,\mathrm{k\Omega}$、$C=10\,\mathrm{nF}$ 对应 $f_c\approx1.59\,\mathrm{kHz}$。试估计元件误差对截止频率的影响。

## 习题

设计一阶低通，用手算、仿真和测量三种手段比对 3 dB 截止频率。

## 应用、实验与验证

用理论和仿真确定元件量级，用实测核对探头和负载对电路的影响。

保存原理图、物料表和仿真测量对照。

## 推导与案例

算出输出负载对低通增益、截止频率和相位的影响。 [推导、案例与练习](推导与案例.md)

## 教材索引

### 教材

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [数字电子技术基础](https://xuanshu.hep.com.cn/front/h5Mobile/bookDetails?bookId=59cf5a91ba9eb884cf822664) | 中文 · 第六版 · 本科 | 逻辑代数、组合逻辑、触发器、时序电路和器件 | 在线入口 |

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [6.002 Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) | 英文 · spring 2007 · 本科 | 电路分析、MOSFET、电路设计和数字抽象 | 在线入口 |
| [6.111 Introductory Digital Systems Laboratory](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/) | 英文 · spring 2006 · 本科 | 数字硬件实验、同步逻辑和项目设计 | 在线入口 |

### 习题

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [6.111 Introductory Digital Systems Laboratory: Assignments](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/pages/assignments/) | 英文 · spring 2006 · 本科 | 数字系统与时序逻辑问题集 | 在线入口 |

### 实验指导

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [6.111 Introductory Digital Systems Laboratory: Labs](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/pages/labs/) | 英文 · spring 2006 · 本科 | 数字调试、时序实验和实验设计；板卡和器件型号依实际平台 | 在线入口 |

### 在线资料

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [KiCad Getting Started](https://docs.kicad.org/) | 英文 · 本科 | 原理图、印制电路板和设计规则 | 在线入口 |
| [KiCad Libraries](https://www.kicad.org/libraries/download/) | 英文 · 本科 | 绘制并验证常见封装；仅资料入口 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/)
- [参考资料 2](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。合上笔记复述知识树，并独立完成本页练习。
- 拓展。将练习结果推广到一种新的条件，记录适用范围。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
