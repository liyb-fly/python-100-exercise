"""
使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
"""


def putNumbers(n):
    i = 0
    while i < n:
        j = i
        i = i + 1
        if j % 7 == 0:
            yield j


x = input("please input 0-?:")
for i in putNumbers(int(x)):
    print(i)
