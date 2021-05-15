# 实例018：复读机相加
# 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

if __name__ == '__main__':
    def method1(a):
        num = int(input("请输入要相加的次数："))
        s = 0
        for i in range(1, num+1):
            n = int(str(a) * i)
            s += n
        print(s)

    def method2(a):
        num = int(input("请输入要相加的次数："))
        s = 0
        n = 0
        for i in range(num):
            n += a * 10 ** i
            s += n
        print(s)


    method1(3)
    method2(3)
    