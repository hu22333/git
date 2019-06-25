# 多输入数字求和
sum = 0
txt = input()
while txt != "":  # ！=为不等于，即说的是当循环输入空值，循环跳出。
    sum += eval(txt)
    txt = input()
print(sum)
