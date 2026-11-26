# 半导体物理

Semiconductor Physics · 学习阶段 3

从材料能带出发解释载流子统计与器件响应。

## 前置知识

[量子力学](../../03-%E5%9B%9B%E5%A4%A7%E5%8A%9B%E5%AD%A6/%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6/README.md)、[热学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E7%83%AD%E5%AD%A6/README.md)

## 章节知识树

1. 能带与有效质量
2. 费米能级与载流子统计
3. 掺杂电中性条件
4. 漂移扩散与连续性方程
5. PN结和平衡与偏置

## 公式与推导

设热平衡下只有同一个费米能级。在非简并近似下，$n=N_c e^{(E_F-E_c)/(k_B T)}$，$p=N_v e^{(E_v-E_F)/(k_B T)}$。相乘后 $E_F$ 消去，得到 $np=N_cN_v e^{-(E_c-E_v)/(k_B T)}=n_i^2$。强注入或重掺杂时要重新检查假设。

## 例题

若 $n_i=10^{10}\,\mathrm{cm}^{-3}$、平衡电子浓度为 $10^{16}\,\mathrm{cm}^{-3}$，则 $p=n_i^2/n=10^4\,\mathrm{cm}^{-3}$。

## 习题

在热平衡、非简并条件下由玻尔兹曼近似推导 n p = n_i²。用理想整流曲线区分正向导通和反向饱和。

## 应用、实验与验证

估算掺杂半导体中的少数载流子，并解释 PN 结模型如何连接电路端口和材料属性。

可先用模拟数据绘制半对数 I–V 曲线，核对理想因子对斜率的影响。

## 教材索引

- 开放课程 · [8.231 Physics of Solids I](https://ocw.mit.edu/courses/8-231-physics-of-solids-i-fall-2006/)
- 开放课程 · [6.012 Microelectronic Devices and Circuits](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/)
- 习题 · [8.231 固体物理问题集](https://ocw.mit.edu/courses/8-231-physics-of-solids-i-fall-2006/pages/assignments/)
- 习题 · [6.012 微电子器件与电路作业](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/pages/assignments/)

## 参考来源

参考教材与公开课程见上方索引。

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。复习时分别写出本征条件、电中性条件、热平衡条件和非简并近似。
- 拓展。研究准费米能级如何描述非平衡载流子。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
