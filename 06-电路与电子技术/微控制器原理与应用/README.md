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

## 专题讲义

[阅读相关推导、例题与自测](../%E4%BB%8E%E7%94%B5%E8%B7%AF%E6%A8%A1%E5%9E%8B%E5%88%B0%E9%87%87%E6%A0%B7%E6%B5%8B%E9%87%8F.md#%E8%AE%A9%E5%BE%AE%E6%8E%A7%E5%88%B6%E5%99%A8%E9%87%87%E6%A0%B7%E5%8F%AF%E4%BB%A5%E5%A4%8D%E6%A0%B8)。

## 教材索引

### 在线资料

| 资源 | 语言与版本 | 对应章节或内容 | 获取 |
| --- | --- | --- | --- |
| [Arduino Built-in Examples](https://docs.arduino.cc/built-in-examples/) | 英文 · 本科 | GPIO、定时、通信和模拟量读写 | 在线入口 |
| [PIC microcontrollers](https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/8-bit-mcus) | 英文 · 本科 | 8 位 MCU 器件文档；核查所用芯片的数据手册 | 在线入口 |

授权与文件校验见 [完整资源清单](../../12-%E6%95%99%E6%9D%90%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%BA%90%E5%BA%93/%E8%B5%84%E6%BA%90%E6%B8%85%E5%8D%95.json)。

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
