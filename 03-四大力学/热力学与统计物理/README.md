# 热力学与统计物理

Thermodynamics and Statistical Physics · 学习阶段 2

从热力学状态函数出发，用统计系综连接微观能级与宏观观测。

## 前置知识

[热学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E7%83%AD%E5%AD%A6/README.md)、[概率论与数理统计](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E6%A6%82%E7%8E%87%E8%AE%BA%E4%B8%8E%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1/README.md)、[高等数学](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/README.md)

## 章节知识树

1. 热力学基本方程、势函数与麦克斯韦关系
2. 稳定性和相平衡
3. 微正则、正则与巨正则系综
4. 经典分布
5. 玻色与费米分布
6. 热容、涨落和相变初步

## 公式与推导

系统与大热库交换能量时，热库熵在平衡点附近展开为 $S_\mathrm{bath}(E_\mathrm{tot}-E_i)\approx S_0-E_i/T$。微观态权重因此正比于 $e^{-\beta E_i}$，除以 $Z=\sum_i e^{-\beta E_i}$ 得归一化概率。

## 例题

能级为 $0,\varepsilon$ 的非简并两态系统，$Z=1+e^{-\beta\varepsilon}$，平均能量 $U=\varepsilon/(e^{\beta\varepsilon}+1)$。高温趋近 $\varepsilon/2$。

## 习题

由正则配分函数对 $\beta$ 求导推出 $\partial_\beta^2\ln Z=\langle E^2\rangle-\langle E\rangle^2$，讨论其与热容的关系。

## 应用、实验与验证

用统计模型理解固体热容、电子分布与热激发过程。

用蒙特卡洛样本估计两态平均能量，与解析正则结果比较。

## 教材索引

- 教材 · [热力学·统计物理](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=5ce43181b0b2bda7c523b60a)
- 教材 · [University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/1-introduction) · [本地文件](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E5%BC%80%E6%94%BE%E6%95%99%E7%A7%91%E4%B9%A6-%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86%E5%AD%A6%E7%AC%AC%E4%BA%8C%E5%8D%B7.pdf)
- 讲义 · [8.044 Statistical Physics I: Lecture 1](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/resources/lecture-notes/) · [本地文件](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E7%BB%9F%E8%AE%A1%E7%89%A9%E7%90%86%E7%AC%AC%E4%B8%80%E8%AE%B2-%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2.pdf)
- 开放课程 · [8.044 Statistical Physics I](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/)
- 习题 · [8.044 统计物理问题集](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/pages/assignments/)
- 开放课程 · [热力学与统计物理](https://www.icourse163.org/course/detail.htm?cid=1450300364)
- 讲义 · [Statistical Physics](https://davidtong.org/teaching/statistical-physics/)

## 参考来源

- [参考资料 1](https://www.damtp.cam.ac.uk/user/tong/statphys.html)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。比较各系综的固定量与涨落量，练习由一个热力学势求响应函数。
- 拓展。延伸到 Ising 模型、临界现象和分子模拟。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
