# 实例016：输出日期
# 输出指定格式的日期。
if __name__ == '__main__':
    import time

    def method1(f, t):
        print(time.strftime(f, t))

    method1("%Y%m%d", time.localtime())

    import datetime

    def method2(f):
        print(datetime.date(2020, 10, 11).strftime(f))

    method2("%Y%m%d")