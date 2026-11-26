# 数字电路

Digital Circuits · 学习阶段 2

用逻辑代数连接真值表和门级结构，再引入时钟、状态和时序约束。

## 前置知识

[电路分析基础](../%E7%94%B5%E8%B7%AF%E5%88%86%E6%9E%90%E5%9F%BA%E7%A1%80/README.md)

## 章节知识树

1. 逻辑电平与布尔代数
2. 组合逻辑、译码和多路复用
3. 加法器、比较器
4. 锁存器和触发器
5. 寄存器、计数器、有限状态机
6. 传播延迟与同步设计

## 公式与推导

全加器和位是三个输入的奇偶校验 $s=a\oplus b\oplus c_\mathrm{in}$。至少两个输入为 1 时才产生进位，因此 $c_\mathrm{out}=ab+ac_\mathrm{in}+bc_\mathrm{in}$。

## 例题

当 $a=1,b=0,c_\mathrm{in}=1$ 时，和位为 $0$，进位为 $1$，二进制结果为 $10_2$。

## 习题

绘制同步模六计数器的状态转移图，说明上电复位和进入未使用状态后的行为。

## 应用、实验与验证

构建实验仪器中的同步采样控制、计数与读出逻辑。

在逻辑仿真中加入传播延迟，检查组合逻辑毛刺与触发器取样时序。

## 专题讲义

[阅读相关推导、例题与自测](../%E4%BB%8E%E7%94%B5%E8%B7%AF%E6%A8%A1%E5%9E%8B%E5%88%B0%E9%87%87%E6%A0%B7%E6%B5%8B%E9%87%8F.md#%E4%BB%8E%E9%80%BB%E8%BE%91%E5%8A%9F%E8%83%BD%E5%88%B0%E6%97%B6%E5%BA%8F%E7%BA%A6%E6%9D%9F)。

## 教材索引

### 教材

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [数字电子技术基础](https://xuanshu.hep.com.cn/front/h5Mobile/bookDetails?bookId=59cf5a91ba9eb884cf822664) | 中文 · 第六版 · 本科 | 逻辑代数、组合逻辑、触发器、时序电路和器件 | 在线入口 |

### 开放课程

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [6.002 Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) | 英文 · spring 2007 · 本科 | 电路分析、MOSFET、电路设计和数字抽象 | 在线入口 |
| [数字电路分析与设计](https://www.icourse163.org/course/ZJU-1205994815) | 中文 · 本科 | 组合逻辑、时序逻辑、触发器 | 在线入口 |
| [6.111 Introductory Digital Systems Laboratory](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/) | 英文 · spring 2006 · 本科 | 数字硬件实验、同步逻辑和项目设计 | 在线入口 |

### 习题

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [数字电子技术基础（第六版）学习辅导与习题解答](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=59cfb25cba9eb884cf82485e) | 中文 · 第六版配套 · 本科 | 按主题学习组合逻辑化简和时序电路分析，核对配套例题 | 在线入口 |
| [6.111 Introductory Digital Systems Laboratory: Assignments](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/pages/assignments/) | 英文 · spring 2006 · 本科 | 数字系统与时序逻辑问题集 | 在线入口 |

### 实验指导

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [6.111 Introductory Digital Systems Laboratory: Labs](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/pages/labs/) | 英文 · spring 2006 · 本科 | 数字调试、时序实验和实验设计；板卡和器件型号依实际平台 | 在线入口 |

### 在线资料

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [KiCad Getting Started](https://docs.kicad.org/) | 英文 · 本科 | 原理图、印制电路板和设计规则 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。根据状态表检查输出依赖当前输入还是状态，并区分时钟周期和路径延迟。
- 拓展。用 HDL 建模并逐步验证同步设计。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
