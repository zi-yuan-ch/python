# 实例005：三数排序
# 题目 输入三个整数x,y,z，请把这三个数由小到大输出。
if __name__ == '__main__':
    # x = int(input("请输入第一个整数："))
    # y = int(input("请输入第二个整数："))
    # z = int(input("请输入第三个整数："))
    #
    # # method1
    # list_num = [x, y, z]
    # list_num.sort()
    # for i in list_num:
    #     print(i)

    # method2
    #
    # if x < y < z:
    #     print(x, y, z)
    # elif x < z < y:
    #     print(x, z, y)
    # elif y < x < z:
    #     print(y, x, z)
    # elif y < z < x:
    #     print(y, z, x)
    # elif z < x < y:
    #     print(z, x, y)
    # else:
    #     print(z, y, x)

    # method3

    def method1(x, y, z):
        list_num = [x, y, z]
        list_num.sort()
        return list_num


    def method2(x, y, z):
        list_num = [x, y, z]
        sorted_num = []
        # 先找到最小的值，存入排序列表
        min_value = min(list_num)
        sorted_num.append(min_value)
        # 把最小值从原列表中移除
        list_num.remove(min_value)
        # 再找出最小值，存入排序列表
        mid_value = min(list_num)
        sorted_num.append(mid_value)
        # 将原列表中最大值，存入排序列表
        sorted_num.append(max(list_num))

        return sorted_num


    def method3(x, y, z):
        def swap(a, b):
            return (min(a, b), max(a, b))

        x, y = swap(x, y)
        y, z = swap(y, z)
        x, y = swap(x, y)
        return x, y, z


    print(method3(2, 3, 1))
