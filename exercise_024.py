# 实例024：斐波那契数列II
# 题目 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。

if __name__ == '__main__':
    fen_zi = 1
    fen_mu = 2
    sum = 0
    for i in range(1, 21):
        sum += fen_mu / fen_zi
        fen_mu, fen_zi = fen_zi + fen_mu, fen_mu
    print(sum)

