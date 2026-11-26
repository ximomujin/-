# 算法与数据结构

Algorithms and Data Structures · 学习阶段 2

用抽象数据结构和复杂度比较可选算法。

## 前置知识

[C 语言程序设计](../C%20%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/README.md)

## 章节知识树

1. 时间和空间复杂度
2. 表、栈与队列
3. 树、堆及散列表
4. 图搜索和最短路
5. 排序及动态规划

## 公式与推导

广度优先搜索把起点放入队列并令其距离为 0。每次出队时，未访问邻点被赋予当前距离加 1 后入队。归纳可知队列中顶点按距离层次被发现，所以得到无权图中边数最少的路径。邻接表实现对每个顶点与每条边最多作常数次处理，复杂度 $O(V+E)$。

## 例题

从 A 出发，在边 A–B、A–C、B–D、C–D 的图中，D 最短距离为 2，可有多个前驱选择。

## 习题

在小型图上手算 BFS 距离，再用相同测试输入校验代码，对照入队与出队次序。

## 应用、实验与验证

对离散网格进行无权最短路径或连通性分析。

上机。针对空输入、孤点与重复数据保留测试样例。

## 教材索引

- 开放课程 · [6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)
- 开放课程 · [6.S096 Introduction to C and C++](https://ocw.mit.edu/courses/6-s096-introduction-to-c-and-c-january-iap-2013/)

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。合上笔记复述知识树，并独立完成本页练习。
- 拓展。将练习结果推广到一种新的条件，记录适用范围。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
