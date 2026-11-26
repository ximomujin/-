# 微控制器原理与应用

Microcontroller Fundamentals and Applications · 学习阶段 3

用定时器、接口和中断实现可测试的嵌入式控制。

## 前置知识

[数字电路](../%E6%95%B0%E5%AD%97%E7%94%B5%E8%B7%AF/README.md)、[C 语言程序设计](../../08-%E7%BC%96%E7%A8%8B%E4%B8%8E%E8%AE%A1%E7%AE%97%E7%89%A9%E7%90%86/C%20%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/README.md)、[电路分析基础](../%E7%94%B5%E8%B7%AF%E5%88%86%E6%9E%90%E5%9F%BA%E7%A1%80/README.md)

## 章节知识树

1. 微控制器结构和寄存器
2. GPIO与定时器
3. 中断和通信接口
4. 传感输入与输出驱动
5. 调试和验证

## 公式与推导

当主时钟 $f_{clk}$ 经分频 $D$ 后进入定时器，一个计数周期耗时 $D/f_{clk}$。在从 0 到比较值 $C$ 后重置且包含端点的模式下，比较事件的周期为 $T=(C+1)D/f_{clk}$。输出在每次比较事件翻转时，输出周期再乘二。

## 例题

若主时钟 16 MHz、分频 64 且比较值 249，则比较事件每 1 ms 发生一次。

## 习题

给定时钟分频和计数上限，推导定时周期并用虚拟逻辑分析仪比对仿真波形。

## 应用、实验与验证

计算周期采样、时钟中断或简单 PWM 的计时参数，并通过仿真核对端点条件。

实验。保留原理图、代码版本、引脚配置和测试记录。

## 教材索引

- 在线资料 · [Arduino Built-in Examples](https://docs.arduino.cc/built-in-examples/)
- 在线资料 · [PIC microcontrollers](https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/8-bit-mcus)

## 参考来源

- [参考资料 1](https://ocw.mit.edu/courses/6-111-introductory-digital-systems-laboratory-spring-2006/)
- [参考资料 2](https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/8-bit-avr/peripherals/timers-counters/8-bit-avr-avrtimerover/)

知识树、推导和题目为 AI 辅助编写的自学内容，专业事实可回查参考资料。

## 复习与拓展

- 复习。合上笔记复述知识树，并独立完成本页练习。
- 拓展。将练习结果推广到一种新的条件，记录适用范围。

## 个人笔记、错题与进度

在此记录自己的推导、实验数据及错因。全库进度见 [学习进度](../../%E5%AD%A6%E4%B9%A0%E8%BF%9B%E5%BA%A6.md)。

| 日期 | 内容 | 证据或改正结果 |
| --- | --- | --- |
