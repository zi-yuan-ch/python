# 实例015：分数归档
# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

if __name__ == '__main__':
    def score_to_grade(score):
        if score >= 90:
            return "A"
        elif score >= 60:
            return "B"
        else:
            return "C"

    print(score_to_grade(50))
