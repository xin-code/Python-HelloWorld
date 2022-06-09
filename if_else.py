
inputScore = input('你的考试成绩是多少？')
# 因为输入进来的为str字符串格式
score = int(inputScore)
# ini是用来字符串转换成整数的函数
if score >= 90:
    print('优秀')
elif score >= 80:
    print('优良')
elif score >= 70:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('重考')
