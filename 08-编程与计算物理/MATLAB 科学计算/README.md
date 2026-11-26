# MATLAB 科学计算

Scientific Computing with MATLAB · 学习阶段 2

用 MATLAB 的数组和矩阵工具表达数值模型。

## 前置知识

[线性代数](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/README.md)

## 章节知识树

1. 数组索引和矩阵运算
2. 脚本和函数
3. 数值求根与线性方程
4. 常微分方程和可视化
5. 读写数据与结果检验

## 公式与推导

当 $A$ 可逆时，近似解 $\hat x$ 的残差为 $r=b-A\hat x$，误差为 $x-\hat x=A^{-1}r$，可推出 $\|x-\hat x\|/\|x\|\le\kappa(A)\|r\|/\|b\|$。因此小残差的解释要结合条件数。

## 例题

用 MATLAB 左除求解 $A=\operatorname{diag}(1,100)$、$b=(1,100)^T$，得到 $x=(1,1)^T$。用 `norm(A*x-b)/norm(b)` 核对相对残差。

## 习题

用 A\b 求解线性方程组，输出相对残差并说明小残差对实际误差的含义受条件数约束。

## 应用、实验与验证

拟合物理数据、求解线性离散系统并记录数值误差。

上机。把代码、测试数据和软件版本一起保存。

## 教材索引

- 开放课程 · [18.335J Introduction to Numerical Methods](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/)
- 习题 · [18.335J 数值方法作业](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/resource-index/)
- 开放课程 · [MATLAB 入门之旅](https://matlabacademy.mathworks.com/cn/details/matlab-onramp/gettingstarted)
- 在线资料 · [MATLAB 帮助中心](https://ww2.mathworks.cn/help/matlab/)

## 参考来源

- [参考资料 1](https://www.mathworks.com/help/matlab/learn_matlab/matrices-and-arrays.html)
- [参考资料 2](https://www.mathworks.com/help/matlab/ref/double.mldivide.html)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。合上笔记复述知识树，并独立完成本页练习。
- 拓展。将练习结果推广到一种新的条件，记录适用范围。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
