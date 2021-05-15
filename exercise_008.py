# 实例008：九九乘法表
# 题目 输出 9*9 乘法口诀表。
# 此题百度了：输出不换行print(“”，end="")

if __name__ == '__main__':
    def method1():
        for i in range(1, 10):
            for j in range(1, i + 1):
                print("{} * {} = {}".format(j, i, i * j), end="  ")
            print()


    method1()