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

## 推导与案例

通过病态线性方程组区分数据扰动、条件数与求解残差。 [推导、案例与练习](推导与案例.md)

## 教材索引

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [18.335J Introduction to Numerical Methods](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/) | 英文 · spring 2019 · 本科 | 数值稳定性、数值线性代数、快速变换 | 在线入口 |
| [MATLAB 入门之旅](https://matlabacademy.mathworks.com/cn/details/matlab-onramp/gettingstarted) | 中文 · 本科 | 矩阵、脚本、数据导入与绘图 | 在线入口 |

### 习题

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [18.335J 数值方法作业](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/resource-index/) | 英文 · spring 2019 · 本科 | 通过课程资源索引访问编程作业 | 在线入口 |

### 在线资料

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [MATLAB 帮助中心](https://ww2.mathworks.cn/help/matlab/) | 中文 · 本科 | 语言语法、线性代数、数值积分、绘图 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

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
