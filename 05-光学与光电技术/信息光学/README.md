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

## 专题讲义

[阅读相关推导、例题与自测](../%E6%B3%A2%E5%8A%A8%E6%88%90%E5%83%8F%E4%B8%8E%E5%85%89%E7%94%B5%E6%B5%8B%E9%87%8F.md#%E4%BB%8E%E5%AD%94%E5%BE%84%E5%BD%A2%E7%8A%B6%E6%89%BE%E8%A1%8D%E5%B0%84%E5%9B%BE%E6%A0%B7)。

## 教材索引

### 教材

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [光学信息技术原理及应用](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=59cd49ceba9eb884cf819b26) | 中文 · 第2版 · 本科 | 傅里叶光学、光学信息处理、全息 | 在线入口 |
| [BSc Optics](https://phys.libretexts.org/Bookshelves/Optics/BSc_Optics_%28Konijnenberg_Adam_and_Urbach%29) | 英文 · 本科 | 波动光学、傅里叶光学和光学成像 | 在线入口 |
| [信号与系统 上册](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=6620017574ce561611bd9ef6) | 中文 · 第四版 · 本科 | 线性时不变系统、时域分析、傅里叶分析和变换域；信息光学用作信号表示参考 | 在线入口 |

### 讲义

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [6.003 Signals and Systems: Lecture Notes](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/lecture-notes/) | 英文 · fall 2011 · 本科 | 卷积、傅里叶与拉普拉斯变换、线性系统、采样 | 在线入口 |

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [2.71 Optics](https://ocw.mit.edu/courses/2-71-optics-spring-2014/) | 英文 · spring 2014 · 本科 | 几何与波动光学、透镜、傅里叶光学与成像设计 | 在线入口 |
| [6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) | 英文 · fall 2011 · 本科 | 信号变换、卷积、抽样及滤波 | 在线入口 |
| [6.637 Optical Signals, Devices, and Systems](https://ocw.mit.edu/courses/6-637-optical-signals-devices-and-systems-spring-2003/) | 英文 · spring 2003 · 本科 | 光信号、光电探测、光学器件、系统噪声与衍射 | 在线入口 |

### 习题

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [2.71 光学习题](https://ocw.mit.edu/courses/2-71-optics-spring-2014/pages/assignments/) | 英文 · spring 2014 · 本科 | 折射与成像、干涉、多缝衍射、傅里叶光学 | 在线入口 |
| [6.637 Optical Signals, Devices, and Systems: Assignments](https://ocw.mit.edu/courses/6-637-optical-signals-devices-and-systems-spring-2003/pages/assignments/) | 英文 · spring 2003 · 本科 | 光信号、传播、光纤和探测相关作业；少量题目依赖指定教材 | 在线入口 |

### 在线资料

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [Meep Documentation](https://meep.readthedocs.io/en/latest/) | 英文 · 本科 | 光传播、衍射和 FDTD 演示；对应课程只作数值拓展。 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

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
