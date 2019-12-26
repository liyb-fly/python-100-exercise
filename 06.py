"""
编写一个以2位X，Y为输入，生成二维数组的程序。数组的第i行和第j列中的元素值应为i*j。

注：i=0,1…，X-1；j=0,1，…Y-1。

例子

假设程序有以下输入：

3,5

那么，程序的输出应该是：

[[0，0，0，0，0]，[0，1，2，3，4]，[0，2，4，6，8]]
"""

x = int(input("请输入行数："))
y = int(input("请输入列数："))
arr__in_list = []
arr__out_list = []
for i in range(x):
    for j in range(y):
        arr__in_list.append(i * j)

    arr__out_list.append(arr__in_list)
    arr__in_list = []

print(arr__out_list)



