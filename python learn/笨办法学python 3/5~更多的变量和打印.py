# ex5.py
my_name = 'Zed A. Shaw'
my_age = 25
my_height = 72
my_weight = 172
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'
# f"..."时为了格式化字符串，使变量在字符串""内部使用，ex4，是属于"..",a,".."的形式
# 字符串嵌入变量需使用{ }
print(f"Let's talk about {my_name}")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actuallty that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair}.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky,try to get it exactly right
total = my_age+my_height+my_weight
print(f"If I add {my_age},{my_height},and {my_weight} I get {total}")
