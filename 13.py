"""
编写一个程序，根据控制台输入的事务日志计算银行帐户的净额。事务日志格式如下：

D 100
W 200

D表示存款，W表示取款。

假设向程序提供了以下输入：

D 300
D 300
W 200
D 100

那么，输出应该是：

500
"""

end = "end"
sum=0
ls = []
a = iter(input, end)
for i in a:
    ls.append(i.split())
for j in ls:

    if j[0] == "D":
        sum += int(j[1])
    else:
        sum -= int(j[1])

print(sum)
