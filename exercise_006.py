# 实例006：斐波那契数列
# 题目 斐波那契数列。

if __name__ == '__main__':
    def fibonacci(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n - 2) + fibonacci(n - 1)


    print(fibonacci(5))