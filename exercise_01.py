# 实例001：数字组合
# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

import itertools

if __name__ == '__main__':
    # method 1
    t = 0
    for a in itertools.permutations([1, 2, 3, 4], 3):
        t += 1
    print('method 1:%d' % t)

    # method 2
    t = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and i != k:
                    t += 1
    print('method 2:{0}'.format(t))
