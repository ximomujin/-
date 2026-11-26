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

## 教材索引

- 开放课程 · [6.002 Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
- 在线资料 · [KiCad Getting Started](https://docs.kicad.org/)
- 在线资料 · [KiCad Libraries](https://www.kicad.org/libraries/download/)

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
