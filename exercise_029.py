# 实例029：反向输出
# 题目 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

if __name__ == '__main__':
    def method(num):
        n = str(num)
        print("{}是{}位数".format(n, str(len(n))))
        print("反向输出为:", str(n[::]))


    method(123356)