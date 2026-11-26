# 光电测量技术

Optoelectronic Measurement · 学习阶段 4

将光信号、探测器、前置电路和标定联系起来建立可追溯的测量链。

## 前置知识

[光学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%85%89%E5%AD%A6/README.md)、[模拟电子技术](../../06-%E7%94%B5%E8%B7%AF%E4%B8%8E%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF/%E6%A8%A1%E6%8B%9F%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF/README.md)

## 章节知识树

1. 辐射量与光度量
2. 光电二极管等探测器
3. 响应度与量子效率
4. 读出与跨阻放大
5. 噪声、带宽和 SNR
6. 调制检测、校准和不确定度

## 公式与推导

单色光功率 $P$ 对应光子流率 $P/(h\nu)$。若每个被探测光子的平均电荷量为 $\eta q$，则 $I=\eta qP/(h\nu)$，响应度 $\mathcal R=I/P=\eta q\lambda/(hc)$。

## 例题

在 $650\,\mathrm{nm}$ 且 $\eta=0.80$ 时，理想响应度约为 $0.42\,\mathrm{A/W}$，需根据器件数据验证。

## 习题

给定暗电流、反馈电阻和探测器响应度，计算所需测量功率范围内的线性输出范围。

## 应用、实验与验证

设计光电功率计和传感读出，并从信号链追踪噪声或饱和。

用教学光电探头做重复测量，分开记录暗电流、零点漂移和参考功率误差。

## 教材索引

- 实验指导 · [The Photoelectric Effect Lab Guide](https://ocw.mit.edu/courses/8-13-14-experimental-physics-i-ii-junior-lab-fall-2016-spring-2017/resources/mit8_13-14f16-s17expi/) · [本地文件](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E5%85%89%E7%94%B5%E6%95%88%E5%BA%94%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC-%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2.pdf)
- 开放课程 · [6.974 Fundamentals of Photonics: Quantum Electronics](https://ocw.mit.edu/courses/6-974-fundamentals-of-photonics-quantum-electronics-spring-2006/)
- 实验指导 · [NIST Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297)
- 在线资料 · [RP Photonics Encyclopedia](https://www.rp-photonics.com/encyclopedia.html)

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/6-101-introductory-analog-electronics-laboratory-spring-2007/)
- [参考资料 2](https://ocw.mit.edu/courses/2-71-optics-spring-2014/)
- [参考资料 3](https://www.itl.nist.gov/div898/handbook/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。统一波长、功率、照度与电信号单位，并核对标定条件。
- 拓展。学习锁相放大、频谱噪声和测量不确定度传播。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
