# C 语言程序设计

C Programming · 学习阶段 1

从数值计算小程序入手，理解 C 的固定类型、内存和编译模型。

## 前置知识

先预习本页概念和术语。

## 章节知识树

1. 编译、类型、表达式与输入输出
2. 分支、循环与函数
3. 数组、指针与字符串
4. 结构体、文件与动态内存
5. 调试、错误处理与数值验证

## 公式与推导

梯形法以区间端点的线性插值近似函数，单区间面积为 $\Delta t(f_i+f_{i+1})/2$。在 C 中用 `double` 累加，显式检查输入长度、文件状态和步长。

## 例题

对 $t=0,1,2$ 的样本 $f=0,1,2$，等步长梯形法给面积 $0.5+1.5=2$。

## 习题

实现读取数据、计算平均值和样本标准差的程序。测试空文件、非数字 token、仅一个数据点以及正常数据。

## 应用、实验与验证

从实验设备导出的文本样本读取数据并输出可复现的汇总表。

上机比较不同数据规模的运行时间，使用编译警告排查类型或下标问题。

## 教材索引

- 教材 · [C语言程序设计教程](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=59ccd2b8ba9eb884cf818344)
- 开放课程 · [6.087 Practical Programming in C](https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/)
- 开放课程 · [6.S096 Introduction to C and C++](https://ocw.mit.edu/courses/6-s096-introduction-to-c-and-c-january-iap-2013/)
- 习题 · [6.087 C 语言问题集](https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/pages/assignments/)
- 教材 · [GNU C Language Introduction and Reference Manual](https://www.gnu.org/software/c-intro-and-ref/manual/html_node/)

## 参考来源

参考教材与公开课程见上方索引。

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。用小数组手工跟踪指针，解释数组越界和整数除法怎样影响物理量。
- 拓展。拓展到 C++ 容器、科学计算库和二进制数据格式。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
