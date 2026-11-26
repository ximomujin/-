# 理论力学

Theoretical Mechanics · 学习阶段 2

用广义坐标和作用量处理带约束的机械系统，再用对称性寻找守恒量。

## 前置知识

[力学](../../02-%E6%99%AE%E9%80%9A%E7%89%A9%E7%90%86%E5%AD%A6/%E5%8A%9B%E5%AD%A6/README.md)、[高等数学](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/README.md)、[线性代数](../../01-%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/README.md)

## 章节知识树

1. 约束、广义坐标和虚位移
2. 达朗贝尔原理
3. 拉格朗日方程和循环坐标
4. 中心力与有效势
5. 刚体及小振动
6. 哈密顿方程和泊松括号

## 公式与推导


[专题推导与习题](%E4%B8%93%E9%A2%98%E6%8E%A8%E5%AF%BC%E4%B8%8E%E4%B9%A0%E9%A2%98.md)提供逐步推导、计算例题和解答。

固定端点的变分满足 $\delta\int L(q,\dot q,t)\,dt=0$。对含 $\delta\dot q$ 的项分部积分，端点项为零，给出 $d(\partial L/\partial\dot q)/dt-\partial L/\partial q=0$。

## 例题

质量 $m$、绳长 $\ell$ 的理想单摆取 $L=\tfrac12m\ell^2\dot\theta^2+mg\ell\cos\theta$。得到 $\ddot\theta+(g/\ell)\sin\theta=0$，小角极限频率为 $\sqrt{g/\ell}$。

## 习题

写出平面中心力系统的拉格朗日量，找出循环坐标和动能中的径向有效项。

## 应用、实验与验证

对机械系统开展模态、轨迹和机器人机构的简化建模。

将单摆数值轨迹与小角解析解比较，检查近似失效时的周期变化。

## 教材索引

### 教材

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [理论力学教程](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=59fdffdbf18f967ee7f364aa) | 中文 · 第四版 · 本科 | 质点与刚体、非惯性系、分析力学 | 在线入口 |

### 讲义

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [8.09 Classical Mechanics III: Advanced Classical Mechanics](https://ocw.mit.edu/courses/8-09-classical-mechanics-iii-fall-2014/resources/lecture-notes/) | 英文 · fall 2014 · 本科 | 分析力学、振动、转动参考系、刚体、流体和混沌 | [离线 PDF](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E9%AB%98%E7%AD%89%E7%BB%8F%E5%85%B8%E5%8A%9B%E5%AD%A6%E8%AE%B2%E4%B9%89-%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2.pdf) |
| [Classical Dynamics](https://davidtong.org/teaching/classical-dynamics/) | 英文 · 本科 | 第 1–4 章；牛顿、拉格朗日、刚体和哈密顿力学 | 在线入口 |

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [8.09 Classical Mechanics III](https://ocw.mit.edu/courses/8-09-classical-mechanics-iii-fall-2014/) | 英文 · fall 2014 · 本科 | 分析力学、振动、刚体与混沌 | 在线入口 |

### 习题

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [8.09 Classical Mechanics III: Problem Set 1](https://ocw.mit.edu/courses/8-09-classical-mechanics-iii-fall-2014/pages/assignments/) | 英文 · fall 2014 · 本科 | 拉格朗日与哈密顿力学复习 | [离线 PDF](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E5%BC%80%E6%94%BE%E6%8E%88%E6%9D%83%E6%96%87%E4%BB%B6/%E7%90%86%E8%AE%BA%E5%8A%9B%E5%AD%A6%E4%B9%A0%E9%A2%98-%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2.pdf) |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

## 参考来源

- [参考资料 1](https://www.damtp.cam.ac.uk/user/tong/dynamics.html)
- [参考资料 2](https://ocw.mit.edu/courses/8-223-classical-mechanics-ii-january-iap-2017/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。先选最少数目的广义坐标，检查量纲后再用守恒量化简。
- 拓展。学习正则变换与辛积分，并比较长期积分的能量漂移。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
