# 实例003：完全平方数
# 题目 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

if __name__ == '__main__':
    #method1
    num = 0
    max_value = 168 * 168
    while num < max_value:
        t1 = int((num + 100) ** 0.5)
        t2 = int((num + 100 + 168) ** 0.5)
        if num + 100 == t1 * t1 and num + 100 + 168 == t2 * t2:
            print(num)
        num += 1

