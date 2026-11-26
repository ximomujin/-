# 普通物理实验二

Introductory Physics Experiments II · 学习阶段 2

通过电学和光学测量验证简化模型及其适用条件。

## 前置知识

[普通物理实验一](../%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AE%9E%E9%AA%8C%E4%B8%80/README.md)、[电磁学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E7%94%B5%E7%A3%81%E5%AD%A6/README.md)、[光学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%85%89%E5%AD%A6/README.md)

## 章节知识树

1. 电学量的测量
2. 仪器量程及负载效应
3. 光路对准与测量
4. 重复性与系统偏差
5. 拟合和残差

## 公式与推导

线性拟合 $y=a x+b$ 时，对无权平方残差和 $\sum_i(y_i-a x_i-b)^2$ 分别按 $a,b$ 求导并令其为零，得到 $a=\sum_i(x_i-\bar x)(y_i-\bar y)/\sum_i(x_i-\bar x)^2$ 及 $b=\bar y-a\bar x$。该式适用于自变量误差可忽略且响应方差近似相同时。

## 例题

给三组数据 $(I,V)=(0,0.1),(1,2.1),(2,4.1)$，若单位分别为 A 和 V，则最佳斜率为 $2\,\Omega$，截距为 $0.1\,\mathrm V$。

## 习题

用模拟 I–V 数据拟合电阻，检查带截距与固定过原点两种模型的残差差异。

## 应用、实验与验证

从拟合截距和残差发现零点偏置、量程切换或测量模型失配。

记录测量或仿真的输入、单位、原始结果及不确定度。

## 教材索引

- 教材 · [大学物理实验](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=6394bdab938b7cc2960ef587)
- 实验指导 · [The Photoelectric Effect Lab Guide](https://ocw.mit.edu/courses/8-13-14-experimental-physics-i-ii-junior-lab-fall-2016-spring-2017/resources/mit8_13-14f16-s17expi/) · [本地文件](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E5%85%89%E7%94%B5%E6%95%88%E5%BA%94%E5%AE%9E%E9%AA%8C%E6%8C%87%E5%AF%BC-%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2.pdf)
- 开放课程 · [8.13–8.14 Experimental Physics I & II](https://ocw.mit.edu/courses/8-13-14-experimental-physics-i-ii-junior-lab-fall-2016-spring-2017/)
- 开放课程 · [大学物理实验](https://www.icourse163.org/course/XJTU-1206492805)
- 实验指导 · [PhET 物理仿真](https://phet.colorado.edu/zh_CN/simulations/filter?subjects=physics)
- 实验指导 · [NIST Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297)

## 参考来源

- [参考资料 1](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e)
- [参考资料 2](https://ocw.mit.edu/courses/8-13-14-experimental-physics-i-ii-junior-lab-fall-2016-spring-2017/pages/experiments/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。合上笔记复述知识树，并独立完成本页练习。
- 拓展。将练习结果推广到一种新的条件，记录适用范围。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
