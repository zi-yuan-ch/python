#
# 实例017：字符串构成
# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 判断一个字符是否是英文字母：isalpha
# 判断一个字符是否是空格，isspace
# 判断一个字符是否是数字：isdigit
if __name__ == '__main__':
    s = input("请输入一串字符：")
    num = 0
    letter = 0
    space = 0
    other = 0
    for i in s:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            letter += 1
        elif i == " ":
            space += 1
        else:
            other += 1
    print(f"字符串{s}中数字{num}个，字母{letter}个，空格{space}个，其他字符{other}个")