# 实例023：画菱形
# 题目 打印出如下图案（菱形）:
#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *
if __name__ == '__main__':
    def method(n):
        ci = 1
        for i in range(0, n):
            if i < n//2:
                print(("*" * ci).center(n))
                ci += 2
            else:
                print(("*" * ci).center(n))
                ci -= 2
    method(7)
    print(('*'*3).center(5,'@'))