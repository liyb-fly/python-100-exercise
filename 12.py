"""
编写一个接受句子的程序，计算大写字母和小写字母的数目。

假设向程序提供了以下输入：

Hello world!
那么，输出应该是：

UPPER CASE 1
LOWER CASE 9
"""
ls = input("please input:")
up = 0
low = 0
for i in ls:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
    else:
        pass
print("UPPER CASE " + str(up))
print("LOWER CASE " + str(low))
