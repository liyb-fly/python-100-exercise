"""
定义至少有两个方法的类：

get string：从控制台输入获取字符串

print string：以大写形式打印字符串。

也请包含简单的测试函数来测试类方法。
"""


class InputOutString(object):

    def __init__(self):
        # 先进行声明
        self.s = ''

    # 获取字符串
    def get_string(self):
        self.s = input('please input:')

    # 输出字符串
    def print_string(self):
        # 将接收到的字符串进行大写
        print(self.s.upper())


# 实例化该对象
str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()
