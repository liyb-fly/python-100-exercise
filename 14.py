"""
网站要求用户输入用户名和密码才能注册。编写程序检查用户输入密码的有效性。
以下是检查密码的条件：
1。[a-z]之间至少有一个字母
2。在[0-9]之间至少有一个数字
1。[A-Z]之间至少有一个字母
3。[$#@]中至少有一个字符
4。交易密码最短长度：6
5。交易密码的最大长度：12
您的程序应该接受一系列逗号分隔的密码，并将根据上述标准进行检查。
将打印符合条件的密码，每个密码用逗号分隔。
例子
如果以下密码作为程序的输入：
ABd1234@1,a F1#,2w3E*,2We3345
那么，程序的输出应该是：
ABd1234@1
"""
import re

pwds = input("please input:")

ls = pwds.split(",")
az = 0
AZ = 0
digit = 0
char_count = 0
for i in ls:
    # 先判断长度
    if len(i) >= 6 and len(i) <= 12:

        # 遍历每一个密码
        for m in i:
            # 使用正则依次进行匹配    并进行相应的计数
            if re.match(r"[a-z]{1,}", m):
                az += 1
            elif re.match(r"[A-Z]{1,}", m):
                AZ += 1

            elif re.match(r"[0-9]{1,}", m):
                digit += 1

            elif re.match(r"[$#@]{1,}", m):
                char_count += 1
            else:
                print("输入了其他字符")

        # 将符合要求的密码进行输出
        if az < 1 or AZ < 1 or digit < 1 or char_count < 1:
            print("%s密码不符合要求" % i)
        else:
            print(i)

        # 计数器置为0
        az = 0
        AZ = 0
        digit = 0
        char_count = 0

