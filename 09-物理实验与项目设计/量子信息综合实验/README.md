# 量子信息综合实验

Integrated Quantum Information Experiments · 学习阶段 4

用量子态及有限计数数据联系理论概率与实验结果。

## 前置知识

[量子力学](../../03-%E5%9B%9B%E5%A4%A7%E5%8A%9B%E5%AD%A6/%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6/README.md)、[线性代数](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/README.md)、[概率论与数理统计](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E6%A6%82%E7%8E%87%E8%AE%BA%E4%B8%8E%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1/README.md)

## 章节知识树

1. 量子态制备和测量
2. 量子门与线路
3. 计数统计和置信区间
4. 仿真对照与噪声
5. 实验记录

## 公式与推导

每次理想独立采样为 Bernoulli 变量。若某结果概率为 $p$，$N$ 次采样的频率 $\hat p$ 方差为 $p(1-p)/N$。区间推断应检查样本量与边界频率。

## 例题

$p=0.5$、$N=100$ 时，理论频率标准差为 $0.05$，可用多轮仿真估计实际波动。

## 习题

用仿真采样 Bell 态计数，比较有限样本频率与理论概率，说明不同随机种子对应的统计波动。

## 应用、实验与验证

比较理想仿真、含噪仿真和实验计数，记录可能的读出偏差。

综合实验。实际装置与项目待课程确认。

## 推导与案例

比较 Bell 态在不同测量基中的奇偶关联及有限样本误差。 [推导、案例与练习](推导与案例.md)

## 教材索引

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [8.370x Quantum Information Science I](https://ocw.mit.edu/courses/8-370x-quantum-information-science-i-spring-2018/) | 英文 · spring 2018 · 本科 | 量子态、量子门、测量和纠缠 | 在线入口 |
| [8.13–8.14 Experimental Physics I & II](https://ocw.mit.edu/courses/8-13-14-experimental-physics-i-ii-junior-lab-fall-2016-spring-2017/) | 英文 · spring 2017 · 本科 | 实验记录、误差和校准、现代物理实验 | 在线入口 |
| [Basics of Quantum Information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information) | 英文 · 本科 | 量子信息基础、复合系统、量子电路和量子纠缠 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

## 参考来源

参考教材与公开课程见上方索引。

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。合上笔记复述知识树，并独立完成本页练习。
- 拓展。将练习结果推广到一种新的条件，记录适用范围。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
