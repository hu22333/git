# 练习一
# Hello World的条件输出
# 获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
# 如果输入值是0，直接输出"Hello World"‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
# 如果输入值大于0，以两个字符一行方式输出"Hello World"（空格也是字符）‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬
# 如果输入值小于0，以垂直方式输出"Hello World"

number = int(input())#需转换为整数类型
# 如直接input()会报错，input()返回的数据类型是str类型（字符串），
# 不能直接和整数进行比较，必须先把str转换成整型
if number < 0:
    print("H\ne\nl\nl\no\n \nW\no\nr\nl\nd")
elif number > 0:
    print("He\nll\no \nWo\nrl\nd")
else:
    print("Hello World")

#答案
n = eval(input())
if n == 0:
    print("Hello World")
elif n > 0:
    print("He\nll\no \nWo\nrl\nd")
else:
    for c in "Hello World":
        print(c)

