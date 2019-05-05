# ex3.py
print("I will now count my chickens:")
# 计算母鸡数量
print("hens", 25+30/6)
# 计算公鸡数量，%为取余
print("roosters", 100-25*3 % 4)
# 多少个鸡蛋
print("Now I will count the eggs:")
print(3+2+1-5+4 % 2-1/4+6)
# 大小关系是否正确
print("Is it true that 3+2<5-7?")
print(3+2 < 5-7)
print("What is 3+2?", 3+2)
print("What is 5-7?", 5-7)
print("Oh,that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 <= -2)

# 练习
# 3计算自己的BMI
height = 1.72
weight = 72
bmi = 72/(1.72*1.72)
print("My BMI is", bmi)
if bmi > 25:
    print('偏重')
else:
    print('正常')
# 4使用浮点数重写ex3.py，使它的计算结果更精确
# (没有女朋友系列)
print('I will now count my girlfriend:')
print("Now I have girlfriend:", 2.0+4.0/2)
print("Is it true?")
money = 1000
if money > 100000:
    print(1000 > 100000)
else:
    print(1000 > 100000)
    pass
print('I have no girlfriend')
print("I don't have a girlfriend now, but I will grow up.")
