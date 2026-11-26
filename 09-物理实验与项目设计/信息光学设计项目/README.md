# 信息光学设计项目

Information Optics Project · 学习阶段 4

以空间频率与衍射模型串起孔径、傅里叶面和像面。

## 前置知识

[数学物理方法](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E6%95%B0%E5%AD%A6%E7%89%A9%E7%90%86%E6%96%B9%E6%B3%95/README.md)、[光学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%85%89%E5%AD%A6/README.md)

## 章节知识树

1. 标量衍射
2. 空间频率和傅里叶面
3. 相干与非相干成像
4. 空间滤波
5. 数值采样与验证

## 公式与推导

取均匀矩形孔径 $A(x)=1$ 于 $|x|<a/2$，其远场振幅正比于 $\int_{-a/2}^{a/2}e^{-2\pi i f_x x}\,dx=a\operatorname{sinc}(a f_x)$，其中 $\operatorname{sinc}(z)=\sin(\pi z)/(\pi z)$。首个零点满足 $f_x=1/a$。

## 例题

若 $\lambda=500\,\mathrm{nm}$、$a=0.1\,\mathrm{mm}$，远场首个零点角满足 $\sin\theta=0.005$，近轴下约 $5\,\mathrm{mrad}$。

## 习题

用离散傅里叶变换展示矩形孔的单缝衍射，比较离散网格中的首零点与理论值。

## 应用、实验与验证

评估空间滤波器并验证 FFT 的坐标、采样和归一化。

注明物面、傅里叶面坐标和采样间隔。

## 教材索引

- 教材 · [光学信息技术原理及应用](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=59cd49ceba9eb884cf819b26)
- 开放课程 · [2.71 Optics](https://ocw.mit.edu/courses/2-71-optics-spring-2014/)
- 在线资料 · [Meep Documentation](https://meep.readthedocs.io/en/latest/)

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
