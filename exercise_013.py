# 实例013：所有水仙花数
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
# 。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
if __name__ == '__main__':
    def method1():
        for i in range(100, 1000):
            x, y, z = map(int, [str(i)[0], str(i)[1], str(i)[2]])
            if i == (x ** 3 + y ** 3 + z ** 3):
                print(i, end='\t')


    def method2():
        for s in range(100, 1000):
            hun = s // 100
            ten = (s % 100) // 10
            one = s % 10
            if s == one ** 3 + ten ** 3 + hun ** 3:
                print(s, end='\t')


    def method3():
        for s in range(100, 1000):
            h = s // 100
            t = s // 10 % 10
            o = s % 10
            if s == o ** 3 + t ** 3 + h ** 3:
                print(s, end='\t')


    method1()
    print()
    method2()
    print()
    method3()
