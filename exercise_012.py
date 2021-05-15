# 实例012：100到200的素数
# 判断101-200之间有多少个素数，并输出所有素数。
# 素数：只能被1和自己整除的数
if __name__ == '__main__':
    def method1():
        count = 0
        for i in range(100, 201):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                count += 1
                print(i, end='\t')


    method1()
