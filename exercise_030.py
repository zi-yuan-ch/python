# 实例030：回文数
# 题目 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

if __name__ == '__main__':
    def method1(n):
        if int(str(n)[0]) == int(str(n)[-1]) and int(str(n)[1]) == int(str(n)[-2]):
            print("%s 是个回文数" % n)
        else:
            print("%s 不是个回文数" % n)


    def method2(num):
        one = num % 10
        ten_thousand = num // 10000
        thousand = num % 10000 // 1000
        ten = num % 10000 % 1000 % 100 // 10
        if one == ten_thousand and ten == thousand:
            print("%s 是个回文数" % num)
        else:
            print("%s 不是个回文数" % num)


    def method3(n):
        s = str(n)
        size = len(s)
        m = size / 2
        l = s[:2]
        r = s[3::].reverse()
        if str(l) == str(r):
            print("%s 是个回文数" % n)
        else:
            print("%s 不是个回文数" % n)


    method1(10301)
    method2(10301)
    method3(10301)
