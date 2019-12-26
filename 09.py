"""
编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字顺序排序后打印这些单词。

假设向程序提供了以下输入：

hello world and practice makes perfect and hello world again

那么，输出应该是：

again and hello makes perfect practice world

"""
a = input("please input:").split(" ")
print(set(a))

b = list(set(a))
b.sort()
print(" ".join(b))
