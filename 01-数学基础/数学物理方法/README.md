# 数学物理方法

Methods of Mathematical Physics · 学习阶段 2

把对称性、边界条件和正交基用于构造物理方程的解。

## 前置知识

[高等数学](../%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/README.md)、[线性代数](../%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/README.md)

## 章节知识树

1. 复变函数、柯西积分与留数
2. 傅里叶级数和傅里叶变换
3. 拉普拉斯变换
4. 常微分方程、特殊函数与正交性
5. 热、波、拉普拉斯方程
6. 分离变量、格林函数和定解问题

## 公式与推导

区间 $0<x<L$ 上的热方程 $\partial_tu=\alpha\partial_x^2u$ 取 $u=XT$，可得 $T'/(\alpha T)=X''/X=-k^2$。齐次固定端温给 $k_n=n\pi/L$，每个温度模态按 $e^{-\alpha k_n^2t}$ 衰减。

## 例题

若初始温差为 $u(x,0)=A\sin(\pi x/L)$，两端固定为零，解仅保留第一模态 $A\sin(\pi x/L)e^{-\alpha\pi^2t/L^2}$。

## 习题

用分离变量求两端固定的理想弦初位形为单个正弦模态时的振动，并核对初始速度。

## 应用、实验与验证

计算温度扩散、腔体频率或位势场，将解析解用于检验数值解。

改变级数截断项数，画出边界附近误差并解释其来源。

## 教材索引

- 教材 · [数学物理方法](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=61704c84938b7cc2960edca7)
- 教材 · [Calculus Volume 2](https://openstax.org/books/calculus-volume-2/pages/1-introduction) · [本地文件](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E5%BC%80%E6%94%BE%E6%95%99%E7%A7%91%E4%B9%A6-%E5%BE%AE%E7%A7%AF%E5%88%86%E7%AC%AC%E4%BA%8C%E5%8D%B7.pdf)
- 开放课程 · [18.04 Complex Variables with Applications](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/)
- 开放课程 · [18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/)
- 习题 · [18.04 复变函数作业](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/problem-sets-and-solutions/)
- 开放课程 · [数学物理方法（一）——复变函数的微积分](https://www.icourse163.org/course/PKU-1003469012)

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。从区域形状和边界条件选择坐标及基函数，记下归一化因子。
- 拓展。学习 Sturm–Liouville 问题、谱方法及有限差分对照。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
