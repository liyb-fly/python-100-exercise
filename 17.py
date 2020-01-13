"""
机器人从原点（0,0）开始在平面内移动。机器人可以向上、下、左、右移动，只要给定步数。机器人运动轨迹如下：
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
方向后面的数字是步数。请写一个程序，计算出一系列运动和原点后距离当前位置的距离。如果距离是浮点数，则只打印最接近的整数。

例子：

如果将下列元组作为程序的输入：
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
那么，程序的输出应该是：
2

"""
import re
import math

# 定义计数器
up = 0
down = 0
left = 0
right = 0

end = "end"
input_str = iter(input, end)
for i in input_str:
    # 进行对应的正则匹配  并且计算计数器的结果  向上为正，下为负   左为正  右为负
    if re.match(r"UP", i):
        for j in i:
            if j.isdigit():
                up += int(j)
            else:
                pass
    elif re.match(r"DOWN", i):
        for j in i:
            if j.isdigit():
                down -= int(j)
            else:
                pass
    elif re.match(r"LEFT", i):
        for j in i:
            if j.isdigit():
                left += int(j)
            else:
                pass
    elif re.match(r"RIGHT", i):
        for j in i:
            if j.isdigit():
                right -= int(j)
            else:
                pass

# 分别计算x方向上和y方向上的步数
x_stick = left + right
y_stick = up + down

# 求平方根
leng_total = math.sqrt(math.pow(x_stick, 2) + math.pow(y_stick, 2))

# 将浮点数转换为整数
print(int(leng_total))
