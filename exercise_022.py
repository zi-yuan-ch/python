# 实例022：比赛对手
# 题目 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

if __name__ == '__main__':
    # 已对对战成员顺序固定，分别是x、y、z
    jia = ['a', 'b', 'c']
    yi = ['x', 'y', 'z']
    for e1 in jia:
        left1 = list(filter(lambda i: i != e1, jia))
        if e1 == 'a' or e1 == 'c':
            continue
        for e2 in left1:
            left2 = list(filter(lambda i: i != e2, left1))
            for e3 in left2:
                if e3 != 'c':
                    print('{0},{1},{2}'.format(e1, e2, e3))

