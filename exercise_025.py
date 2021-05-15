# 实例025： 阶乘求和
# 题目 求1+2!+3!+…+20!的和。

if __name__ == '__main__':
    def method(n):
        if n == 1:
            return 1
        else:
            return n * method(n - 1)


    # 作用同method
    def method2(m, n):
        if n <= 1:
            return m
        return method2(m * n, n - 1)


    # 直接计算阶乘求和
    def method3(n):
        arr = [1 for _ in range(0, n)]
        for i in range(2, n + 1):
            arr[i - 1] = arr[i - 2] * i
        return sum(arr)


    total = 0
    for i in range(1, 21):
        total += method(i)
    print(total)
    print(method3(20))

    # print(method(3))
    # print(method2(1, 3))
