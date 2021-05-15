# 实例004：这天第几天
# 题目 输入某年某月某日，判断这一天是这一年的第几天？
if __name__ == '__main__':
    # method1
    def date_to_days(date):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split("-"))
        total = 0
        for i in range(0, m-1):
            total += days[i]
            if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) and i == 1:
                total += 1
        return total + d

    date = input("请输入日期，例：2020-10-21：")
    t = date_to_days(date)
    print("{}是这一年的第{}天".format(date, t))
