# 实例010：给人看的时间
# 题目 暂停一秒输出，并格式化当前时间。

if __name__ == '__main__':
    # method1
    import time

    print("当前时间为：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(1)
    print("暂停1秒后时间为：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
