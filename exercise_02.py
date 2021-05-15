# 实例002：“个税计算”
# 题目 企业发放的奖金根据利润提成。
# 利润低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

if __name__ == '__main__':
    def method1(n):
        award = 0.0
        # 利润低于或等于10万元时，奖金可提10%
        m = [10, 10, 20, 20, 40]
        rate = [0.1, 0.075, 0.05, 0.03, 0.015]

        l1 = 10
        l2 = 20
        l3 = 40
        l4 = 60
        l5 = 100

        # 小于10万
        if n <= l1:
            award += n * 0.1
            return award

        # 10-20万
        award += l1 * 0.1
        if n <= l2:
            award += (n - l1) * 0.075
            return award

        # 20-40万
        award += (l2 - l1) * 0.075
        if n <= l3:
            award += (n - l2) * 0.05
            return award

        # 40-60万
        award += (l3 - l1) * 0.05
        if n <= l4:
            award += (n - l3) * 0.03
            return award

        # 60-100万
        award += (l4 - l3) * 0.03
        if n <= l5:
            award += (n - l4) * 0.015
            return award

        # 100万以上
        award += (n - l5) * 0.01
        return award


    def method2(i):
        total_bonus = 0
        m = [10, 10, 20, 20, 40]
        rate = [0.1, 0.075, 0.05, 0.03, 0.015]
        if i <= 10:
            total_bonus = i * rate[0]
        elif i <= 20:
            total_bonus = (i - 10) * rate[1] + m[0] * rate[0]
        elif i <= 40:
            total_bonus = (i - 20) * rate[2] + m[1] * rate[1] + m[0] * rate[0]
        elif i <= 60:
            total_bonus = (i - 40) * rate[3] + m[2] * rate[2] + m[1] * rate[1] + m[0] * rate[0]
        elif i <= 100:
            total_bonus = (i - 60) * rate[4] + m[3] * rate[3] + m[2] * rate[2] + m[1] * rate[1] + m[0] * rate[0]
        else:
            total_bonus = (i - 100) * 0.1 + m[4] * rate[4] + m[3] * rate[3] + m[2] * rate[2] + m[1] * rate[1] + m[0] * \
                          rate[
                              0]
        return total_bonus


    a = int(input())
    print(method1(a))
    print(method2(a))
