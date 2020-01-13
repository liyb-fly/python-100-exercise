"""
编写一个接受句子并计算字母和数字的程序。

假设向程序提供了以下输入：

hello world! 123

那么，输出应该是：

LETTERS 10
DIGITS 3
"""

ls = input("please input:")
digit = 0
alpha = 0
for i in ls:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1

print("LETTERS " + str(alpha))
print("DIGITS " + str(digit))

