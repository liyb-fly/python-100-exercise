"""
编写一个程序，根据给定的公式计算并打印值：

Q= [(2 * C * D)/H]的平方根

C和H的固定值如下：

C是50。H是30。

D是一个变量，其值应以逗号分隔的顺序输入到程序中。

例子

假设程序有以下逗号分隔的输入序列：

100,150,180

程序的输出应为：

18，22，24

"""
import math


class InputOutMap(object):
    def __init__(self):
        self.C = 50
        self.H = 30
        self.s = ''
        self.b = []
        pass

    # 定义输入方法
    def input(self):
        self.s = input('please input:')

    # 定义计算
    def handle(self):
        # 将接受到的数字转换为列表
        a = self.s.split(',')

        # 遍历列表，进行计算
        for D in a:
            Q = str(round(math.sqrt((2 * self.C * int(D)) / self.H)))
            self.b.append(Q)

    # 定义输出方法
    def out(self):
        # 将结果b列表进行转换字符串
        print(','.join(self.b))


obj = InputOutMap()
obj.input()
obj.handle()
obj.out()
