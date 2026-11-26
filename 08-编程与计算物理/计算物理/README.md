# 计算物理

Computational Physics · 学习阶段 3

把物理模型转换成可验证的数值程序。

## 前置知识

[高等数学](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/README.md)、[线性代数](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/README.md)、[力学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%8A%9B%E5%AD%A6/README.md)、[C 语言程序设计](../C%20%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/README.md)

## 章节知识树

1. 截断误差与浮点误差
2. 插值、积分和求根
3. 常微分方程时间推进
4. 扩散方程差分及稳定性
5. 蒙特卡洛与可复现实验

## 公式与推导

对扩散方程 $u_t=D u_{xx}$ 使用前向时间差分和中心空间差分。得到 $u_j^{n+1}=u_j^n+r(u_{j+1}^n-2u_j^n+u_{j-1}^n)$。其中 $r=D\Delta t/\Delta x^2$。傅里叶模放大因子为 $1-4r\sin^2(k\Delta x/2)$，由模不超过 1 得一维均匀网格常系数情形下 $0\le r\le1/2$。

## 例题

$D=1\,\mathrm{m^2/s}$ 且 $\Delta x=0.1\,\mathrm m$ 时，一维显式格式取 $\Delta t\le0.005\,\mathrm s$。试用解析初始正弦模核验衰减率。

## 习题

用解析简谐振子检验一阶欧拉与四阶龙格—库塔，画最大误差随步长变化的双对数图并估计斜率。

## 应用、实验与验证

用时间步或网格加密对照解析解，检查收敛阶和误差瓶颈。

上机。每份报告保留量纲、输入、误差和验证结果。

## 教材索引

- 开放课程 · [12.010 Computational Methods of Scientific Programming](https://ocw.mit.edu/courses/12-010-computational-methods-of-scientific-programming-fall-2024/)
- 开放课程 · [18.335J Introduction to Numerical Methods](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/)
- 习题 · [18.335J 数值方法作业](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/resource-index/)
- 教材 · [Python 教程](https://docs.python.org/zh-cn/3/tutorial/)
- 教材 · [Think Python](https://allendowney.github.io/ThinkPython/)
- 开放课程 · [MATLAB 入门之旅](https://matlabacademy.mathworks.com/cn/details/matlab-onramp/gettingstarted)
- 在线资料 · [MATLAB 帮助中心](https://ww2.mathworks.cn/help/matlab/)
- 在线资料 · [SciPy User Guide](https://docs.scipy.org/doc/scipy/tutorial/)

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/)
- [参考资料 2](https://numpy.org/doc/stable/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。复习一致性、稳定性和收敛性，区别模型误差、截断误差与浮点误差。
- 拓展。比较显式与隐式扩散格式的稳定性和单步成本。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
