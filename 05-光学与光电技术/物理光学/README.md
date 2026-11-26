# 物理光学

Physical Optics · 学习阶段 3

用复振幅和波动传播说明空间衍射、相干叠加及偏振。

## 前置知识

[光学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%85%89%E5%AD%A6/README.md)、[数学物理方法](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E6%95%B0%E5%AD%A6%E7%89%A9%E7%90%86%E6%96%B9%E6%B3%95/README.md)

## 章节知识树

1. 平面波与球面波
2. 相干与干涉
3. 惠更斯–菲涅尔积分
4. 菲涅尔和夫琅禾费衍射
5. 光栅、孔径及分辨率
6. 偏振矩阵和波片

## 公式与推导

远场单缝的复振幅正比于矩形孔径的傅里叶变换。积分 $\int_{-a/2}^{a/2}e^{-ikx\sin\theta}dx$ 得 $\mathrm{sinc}(\pi a\sin\theta/\lambda)$ 型振幅，强度为该函数的模平方。

## 例题

若 $a=0.10\,\mathrm{mm}$，$\lambda=500\,\mathrm{nm}$，一级暗纹小角满足 $\theta\approx 5.0\,\mathrm{mrad}$。

## 习题

计算单缝宽度加倍时主瓣角宽度与远场分布的变化，再说明归一化强度图能提供哪些信息。

## 应用、实验与验证

解释孔径限制带来的分辨率下降，设计衍射测量的采样与标定方案。

将单缝强度截面拟合为 sinc 平方函数；核对背景扣除和原点位置。

## 专题讲义

[阅读相关推导、例题与自测](../%E6%B3%A2%E5%8A%A8%E6%88%90%E5%83%8F%E4%B8%8E%E5%85%89%E7%94%B5%E6%B5%8B%E9%87%8F.md#%E4%BB%8E%E5%AD%94%E5%BE%84%E5%BD%A2%E7%8A%B6%E6%89%BE%E8%A1%8D%E5%B0%84%E5%9B%BE%E6%A0%B7)。

## 教材索引

### 教材

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [新概念物理教程 光学](https://abook.hep.com.cn/1254524) | 中文 · 第二版 · 本科 | 几何光学、干涉、衍射、偏振与现代光学 | 在线入口 |
| [University Physics Volume 3](https://openstax.org/books/university-physics-volume-3/pages/1-introduction) | 英文 · 2026 PDF（版权页） · 本科 | Ch. 1–4 光学；Ch. 5–9 现代物理及凝聚态入门；Ch. 10–11 核和粒子入门 | [离线 PDF](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E5%BC%80%E6%94%BE%E6%95%99%E7%A7%91%E4%B9%A6-%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86%E5%AD%A6%E7%AC%AC%E4%B8%89%E5%8D%B7.pdf) |
| [BSc Optics](https://phys.libretexts.org/Bookshelves/Optics/BSc_Optics_%28Konijnenberg_Adam_and_Urbach%29) | 英文 · 本科 | 波动光学、傅里叶光学和光学成像 | 在线入口 |

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [8.03SC Physics III: Vibrations and Waves](https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/) | 英文 · fall 2016 · 本科 | 波动方程、振动与光学 | 在线入口 |
| [2.71 Optics](https://ocw.mit.edu/courses/2-71-optics-spring-2014/) | 英文 · spring 2014 · 本科 | 几何与波动光学、透镜、傅里叶光学与成像设计 | 在线入口 |

### 习题

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [8.03SC 振动与波练习总索引](https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/resource-index/) | 英文 · fall 2016 · 本科 | 振动、散射、干涉与衍射 | 在线入口 |
| [2.71 光学习题](https://ocw.mit.edu/courses/2-71-optics-spring-2014/pages/assignments/) | 英文 · spring 2014 · 本科 | 折射与成像、干涉、多缝衍射、傅里叶光学 | 在线入口 |

### 在线资料

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [Meep Documentation](https://meep.readthedocs.io/en/latest/) | 英文 · 本科 | 光传播、衍射和 FDTD 演示；对应课程只作数值拓展。 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

## 参考来源

- [参考资料 1](https://openstax.org/details/books/university-physics-volume-3)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。检查相干性、标量近似和远场条件，区分归一化振幅与归一化强度。
- 拓展。用数值传播比较近场和远场，学习空间相干函数。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
