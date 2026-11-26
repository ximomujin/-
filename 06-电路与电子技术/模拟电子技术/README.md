# 模拟电子技术

Analog Electronics · 学习阶段 2

从器件工作点分析小信号响应，再用反馈构造稳定、可测的模拟功能。

## 前置知识

[电路分析基础](../%E7%94%B5%E8%B7%AF%E5%88%86%E6%9E%90%E5%9F%BA%E7%A1%80/README.md)

## 章节知识树

1. 二极管与整流
2. BJT、MOSFET 及直流偏置
3. 小信号模型和单级放大
4. 差分输入与运算放大器
5. 负反馈、频率响应与稳定性
6. 滤波与实验测量

## 公式与推导

理想运放在线性负反馈区内有 $v_-\approx v_+$、输入电流近零。反相放大器令 $v_+=0$，由反相节点 KCL 得 $v_o/v_i=-R_f/R_\mathrm{in}$。输入共模、带宽和输出摆幅仍需检查。

## 例题

令 $R_f=100\,\mathrm{k\Omega}$、$R_\mathrm{in}=10\,\mathrm{k\Omega}$。若运放在线性区，$0.1\,\mathrm V$ 输入对应 $-1\,\mathrm V$ 输出。

## 习题

计算同相放大器闭环增益，给定实际运放增益带宽积后估计小信号带宽。

## 应用、实验与验证

构造用于光电传感器或实验仪器的输入放大级和有源滤波器。

用教学实验板量测小信号增益和失真出现的幅度，记录供电与频率。

## 教材索引

- 教材 · [模拟电子技术基础](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=619e6fa2938b7cc2960edde5)
- 开放课程 · [6.002 Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/)
- 开放课程 · [6.012 Microelectronic Devices and Circuits](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/)
- 习题 · [6.012 微电子器件与电路作业](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/pages/assignments/)
- 开放课程 · [模拟电子技术基础](https://www.icourse163.org/course/XJTU-1001807015)
- 在线资料 · [KiCad Getting Started](https://docs.kicad.org/)

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。每次先核对器件工作区和反馈极性，再选等效模型。
- 拓展。比较运放电压偏置、输入电流、噪声和跨阻反馈对弱信号测量的影响。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
