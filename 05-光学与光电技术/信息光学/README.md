# 信息光学

Information Optics · 学习阶段 4

将光学成像视为对空间频率的变换与筛选，比较相干与非相干成像。

## 前置知识

[光学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%85%89%E5%AD%A6/README.md)、[数学物理方法](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E6%95%B0%E5%AD%A6%E7%89%A9%E7%90%86%E6%96%B9%E6%B3%95/README.md)、[物理光学](../%E7%89%A9%E7%90%86%E5%85%89%E5%AD%A6/README.md)

## 章节知识树

1. 二维傅里叶变换与卷积
2. 傅里叶透镜和焦平面
3. 相干成像与振幅传递函数
4. 非相干成像、点扩散函数和 OTF
5. 空间滤波与全息
6. 离散采样和数字重建

## 公式与推导

对相干 4f 系统，傅里叶面滤波器 $H(f_x,f_y)$ 乘到入射复振幅的空间谱。回到像面得到 $u_\mathrm{out}=u_\mathrm{in}*h$，其中 $h=\mathcal F^{-1}H$，假设近轴、线性且空间不变。

## 例题

压低高空间频率会使锐利边缘变宽。放行含方向选择的频率区域会沿特定方向改变纹理。

## 习题

对二维棋盘图像执行理想低通滤波，改变截止频率并解释边缘振铃。

## 应用、实验与验证

以空间滤波实现边缘提取，或用点扩散函数评估光学成像质量。

用 FFT 模拟相干成像，检查采样间隔、像素单位和能量归一化。

## 教材索引

- 教材 · [光学信息技术原理及应用](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=59cd49ceba9eb884cf819b26)
- 开放课程 · [2.71 Optics](https://ocw.mit.edu/courses/2-71-optics-spring-2014/)
- 开放课程 · [6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/)
- 习题 · [2.71 光学习题](https://ocw.mit.edu/courses/2-71-optics-spring-2014/pages/assignments/)
- 教材 · [BSc Optics](https://phys.libretexts.org/Bookshelves/Optics/BSc_Optics_(Konijnenberg_Adam_and_Urbach))
- 在线资料 · [Meep Documentation](https://meep.readthedocs.io/en/latest/)

## 参考来源

参考教材与公开课程见上方索引。

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。先明确传播的是振幅还是强度，再选择传递函数。
- 拓展。延伸到数字全息、相位恢复及反卷积。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
