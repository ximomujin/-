# 电动力学

Electrodynamics · 学习阶段 3

用麦克斯韦方程、势和边界条件处理时变的电磁场。

## 前置知识

[电磁学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E7%94%B5%E7%A3%81%E5%AD%A6/README.md)、[高等数学](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/README.md)、[数学物理方法](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E6%95%B0%E5%AD%A6%E7%89%A9%E7%90%86%E6%96%B9%E6%B3%95/README.md)

## 章节知识树

1. 电磁场方程与边界条件
2. 静电和静磁边值问题
3. 规范、标势和矢势
4. 平面电磁波与能流
5. 波导、介质及反射透射
6. 推迟势、辐射和相对论形式

## 公式与推导

真空无源区满足 $\nabla\times\mathbf E=-\partial_t\mathbf B$、$\nabla\times\mathbf B=\mu_0\epsilon_0\partial_t\mathbf E$ 和 $\nabla\cdot\mathbf E=0$。对第一式取旋度并代入其余方程，得 $\nabla^2\mathbf E-\mu_0\epsilon_0\partial_t^2\mathbf E=0$。

## 例题

真空平面波的峰值 $E_0=30\,\mathrm{V/m}$ 时，$B_0=E_0/c\approx 1.0\times10^{-7}\,\mathrm T$。

## 习题

推导垂直入射于两种非磁、无吸收介质界面时的电场振幅反射系数，并用能流验证守恒。

## 应用、实验与验证

评估波导截止、天线辐射与介质界面上的反射。

用离散网格求二维静电势，比较不同边界与网格尺寸下的解。

## 教材索引

- 教材 · [电动力学](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=620150dd938b7cc2960ee60d)
- 教材 · [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/1-introduction) · [本地文件](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E5%BC%80%E6%94%BE%E6%95%99%E7%A7%91%E4%B9%A6-%E5%BE%AE%E7%A7%AF%E5%88%86%E7%AC%AC%E4%B8%89%E5%8D%B7.pdf)
- 开放课程 · [8.07 Electromagnetism II](https://ocw.mit.edu/courses/8-07-electromagnetism-ii-fall-2012/)
- 习题 · [8.07 电动力学问题集](https://ocw.mit.edu/courses/8-07-electromagnetism-ii-fall-2012/pages/assignments/)
- 开放课程 · [电动力学](https://www.icourse163.org/course/0702SCNU008-1003540137)
- 讲义 · [Electromagnetism](https://davidtong.org/teaching/electromagnetism/)
- 教材 · [Essential Graduate Physics: Classical Electrodynamics](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Essential_Graduate_Physics_-_Classical_Electrodynamics_(Likharev))

## 参考来源

- [参考资料 1](https://www.damtp.cam.ac.uk/user/tong/em.html)
- [参考资料 2](https://openstax.org/details/books/university-physics-volume-2)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。从 Maxwell 方程说明每个约束条件，检查场方向、复振幅和能流单位。
- 拓展。学习电磁有限差分时域法和辐射多极展开。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
