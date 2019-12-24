"""
写一个能计算给定 数的阶乘的程序。

结果应以逗号分隔的顺序打印在一行上。

假设向程序提供了以下输入：

8

那么，输出应该是：

40320
"""

a = int(input('input the number:'))
JC = int(1)
while a != 0:
    JC = JC * a
    a -= 1

print(JC)
