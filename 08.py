"""
编写一个程序，接受行序列作为输入，并在将句子中的所有字符大写后打印行。
假设向程序提供了以下输入：
Hello world
Practice makes perfect
那么，输出应该是：
HELLO WORLD
PRACTICE MAKES PERFECT
"""

ls = []
end = 'end'
print("输入,并以end结束")
for i in iter(input, end):
    ls.append(i.upper())
print(ls)



# 知识点：iter使用


