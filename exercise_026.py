# 实例026：递归求阶乘
# 题目 利用递归方法求5!。

if __name__ == '__main__':
    def method1(n):
        if n == 1:
            return 1
        else:
            return n * method1(n - 1)


    def method2(m, n):
        if n <= 1:
            return m
        else:
            return method2(m * n, n - 1)


    print(method1(5))
    print(method2(1, 5))

    print(('*' * 5).center(7,))
