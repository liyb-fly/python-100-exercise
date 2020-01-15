"""
定义一个函数，该函数可以生成和打印一个元组，其中的值是介于1和20之间（两者都包括在内）的数字的平方。
"""


# 将列表转换为元组
def f():
    a = []
    for i in range(1, 21):
        a.append(i ** 2)

    b = tuple(a)

    return b


print(f())
