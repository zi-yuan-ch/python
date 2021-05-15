# 实例019：完数
# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 什么是完数？？？他所有的真因子（除本身外的所有约数）的和，恰好等于他本身
if __name__ == '__main__':
    def method1():
        for i in range(1, 1000):
            s = 0
            for j in range(1, i):
                if i % j == 0:
                    s += j
            if i == s:
                print(i)


    method1()