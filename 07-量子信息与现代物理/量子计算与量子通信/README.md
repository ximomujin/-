# 量子计算与量子通信

Quantum Computation and Quantum Communication · 学习阶段 4

以量子态、测量和线路为基础理解量子计算与通信。

## 前置知识

[线性代数](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/README.md)、[量子力学](../../03-%E5%9B%9B%E5%A4%A7%E5%8A%9B%E5%AD%A6/%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6/README.md)、[概率论与数理统计](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E6%A6%82%E7%8E%87%E8%AE%BA%E4%B8%8E%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1/README.md)

## 章节知识树

1. 量子比特和布洛赫球
2. 复合系统和纠缠
3. 常见量子门与线路
4. 测量、通信协议和噪声
5. 简单算法与资源估算

## 公式与推导

将矩阵 $H\otimes I$ 作用于 $|00\rangle$，得 $(|00\rangle+|10\rangle)/\sqrt2$。CNOT 保持 $|00\rangle$ 并将 $|10\rangle$ 映射到 $|11\rangle$，输出 $|\Phi^+\rangle$。Born 概率由对应振幅的模方给出。

## 例题

对理想 Bell 态分别做 1000 次计算基采样时，$00$ 和 $11$ 的期望计数各为 500，单项计数的标准差为 $\sqrt{250}\approx15.8$。

## 习题

在 |00⟩ 上对首位施加 H 门，再施加 CNOT，手算两个测量比特的联合分布。结果为 00 与 11 各半。

## 应用、实验与验证

检查量子线路仿真的概率归一、位序和多次采样结果。

通过矩阵乘法复现 Bell 态线路，核对概率归一和位序约定。

## 教材索引

- 开放课程 · [8.370x Quantum Information Science I](https://ocw.mit.edu/courses/8-370x-quantum-information-science-i-spring-2018/)
- 开放课程 · [Basics of Quantum Information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information)

## 参考来源

参考教材与公开课程见上方索引。

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。区分张量积、叠加和纠缠，并掌握振幅与概率的不同运算。
- 拓展。比较 Bell 态和经典相关混合态在不同测量基下的结果。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
