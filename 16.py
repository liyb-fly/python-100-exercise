"""
您需要编写一个程序来按升序对（name，age，height）元组进行排序，其中name是string，age和height是数字。元组由控制台输入。排序条件为：

1：按名称排序；

2:然后按年龄排序；

3:然后按分数排序。

优先考虑的是名字>年龄>分数。

如果将下列元组作为程序的输入：

Tom,19,80
John,20,90
Jony,17,91
Jony,18,91
Jony,17,93
Json,21,85

那么，程序的输出应该是：

[(‘John’, ‘20’, ‘90’), (‘Jony’, ‘17’, ‘91’), (‘Jony’, ‘17’, ‘93’), (‘Json’, ‘21’, ‘85’), (‘Tom’, ‘19’, ‘80’)]
"""
import operator

end = "end"
ls = []
for i in iter(input, end):
    ls.append(tuple(i.split(",")))

print(sorted(ls, key=operator.itemgetter(0, 2, 1)))
print(sorted(ls, key=operator.itemgetter(0, 1, 2)))


