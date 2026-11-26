# 现代光学设计

Optical System Design · 学习阶段 3

从近轴系统的成像条件建立可计算模型，再讨论像差、容差与优化目标。

## 前置知识

[光学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%85%89%E5%AD%A6/README.md)

## 章节知识树

1. 光线、折射和光线传递矩阵
2. 共轭成像与放大率
3. 光阑、光瞳、焦深和数值孔径
4. 单色及色像差
5. 成像质量指标
6. 光线追迹、优化和容差

## 公式与推导

空气中使用光线向量 $(y,\theta)$。传播距离 $d$ 与薄透镜焦距 $f$ 分别对应 $P(d)=\begin{pmatrix}1&d\\0&1\end{pmatrix}$ 和 $L(f)=\begin{pmatrix}1&0\\-1/f&1\end{pmatrix}$。乘积 $P(s')L(f)P(s)$ 的 $B$ 元素取零时，同一物点的不同初始方向在像面相交，从而得到 $1/s+1/s'=1/f$。

## 例题

$s=2f$ 时近轴成像为 $s'=2f$，横向放大率 $-1$。

## 习题

用矩阵求两枚相同焦距薄透镜相隔 $2f$ 的系统在两端焦平面之间的光线变换。

## 应用、实验与验证

初步估计照明、成像或探测系统的焦距、孔径和视场。

用光线追迹比较近轴近似与大角度光线的像点差异。

## 教材索引

- 开放课程 · [2.71 Optics](https://ocw.mit.edu/courses/2-71-optics-spring-2014/)
- 习题 · [2.71 光学习题](https://ocw.mit.edu/courses/2-71-optics-spring-2014/pages/assignments/)
- 教材 · [BSc Optics](https://phys.libretexts.org/Bookshelves/Optics/BSc_Optics_(Konijnenberg_Adam_and_Urbach))
- 在线资料 · [2.71 光学教学大纲](https://ocw.mit.edu/courses/2-71-optics-spring-2014/pages/syllabus/)
- 在线资料 · [Meep Documentation](https://meep.readthedocs.io/en/latest/)
- 在线资料 · [RP Photonics Encyclopedia](https://www.rp-photonics.com/encyclopedia.html)

## 参考来源

- [参考资料 1](https://openstax.org/details/books/university-physics-volume-3)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。统一距离和角度的符号约定，检查传播矩阵的相乘顺序。
- 拓展。学习调制传递函数、优化权重和误差预算。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
