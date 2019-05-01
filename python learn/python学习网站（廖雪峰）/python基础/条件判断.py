age = 25
if age >= 18:  # 注意有：号
    print('hu is', age)  # 注意要缩进
    print('adult')
elif age <= 6:
    print('hu is', age)
    print('teenager')
else:
    print('kid')

# 练习：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 改成自己的数据进行计算
height = 1.72
weight = 72
bmi = 72/(1.72*1.72)
if bmi < 18.5:
    print('小胡的BMI为', bmi)
    print('过轻')
elif 18.5 <= bmi <= 25:
    print('小胡的BMI为', bmi)
    print('正常')
elif 25 < bmi < 28:
    print('小胡的BMI为', bmi)
    print('过重')
elif 28 <= bmi <= 32:
    print('小胡的BMI为', bmi)
    print('肥胖')
else:
    print('小胡的BMI为', bmi)
    print('严重肥胖')
    pass
