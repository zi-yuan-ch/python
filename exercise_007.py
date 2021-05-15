# 实例007：copy
# 题目 将一个列表的数据复制到另一个列表中。


if __name__ == '__main__':

    # # method1
    # def copy_list(target_list):
    #     list_copy = []
    #     for i in target_list:
    #         list_copy.append(i)
    #     return list_copy
    #
    #
    # target_list = [2, 3, 5, 10, "ui"]
    # print(target_list)
    #
    # # method2
    # target_list_1 = [2, 3, 1, "839", "hssj"]
    # copy_list_1 = target_list_1.copy()
    # print(copy_list_1)

    # method3
    t3 = [1, 2, 'a', 'b']
    copy3 = t3[:]
    t3[1] = 3
    print(copy3)
