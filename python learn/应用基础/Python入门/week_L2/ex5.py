# 多输入均值
# me
a = input()
ls = a.split()
n = len(ls)
avg = 0
for out in ls:
    avg += eval(out)
    c = avg/n
print("{:.1f}".format(c))

# 答案
txt = input()
ls = txt.split()
sum = 0
for item in ls:
    sum += eval(item)
print("{:.1f}".format(sum/len(ls)))
