"""
写一个程序从输入中计算单词的频率。输出应该在按字母数字顺序对键排序后输出。

假设向程序提供了以下输入：

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

那么，输出应该是：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

"""

i_count = 0
input_str = input("please input:")

input_list = input_str.split(" ")
for i in input_list:
    # 在这里遍历两次该列表，进行对比 ， 然后进行计数器的累加
    for j in input_list:
        if i == j:
            i_count += 1
    print("%s:%s" % (i, i_count))
    i_count = 0

