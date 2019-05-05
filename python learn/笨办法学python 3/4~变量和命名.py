#ex4.py
cars=100 #将100赋值给cars变量
space_in_a_car=4.0 #将4.0赋值给space_in_a_car变量
drivers=30 #将30赋值给drivers变量
passengers=90 #将90赋值给passengers变量
cars_not_driver=cars-drivers #cars变量的值减drivers变量的值（100-30=70）赋值给cars_not_driver
cars_driven=drivers #将drivers的值赋值给cars_driven变量（30）
carpool_capactiy=cars_driven*space_in_a_car #将。。。变量的值幅值给carpool_capactiy（30*4.0=120.0）
average_passengers_per_car=passengers/cars_driven #将。。。变量的值幅值给average_passengers_per_car（90/30=3）
#打印变量并描述
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driver,"empty cars today.")
print("we can transport",carpool_capactiy,"people today.")
print("we have",passengers,"to carppp; today.")
print("We need to put about",average_passengers_per_car,"in each car.")

#练习
#1若space_in_a_car=4
# print("we can transport",carpool_capactiy,"people today.") 
#结果输出120，而变量为4.0结果为120.0
#4 =的名字是等于，作用是为数据(数值、字符串)取名
#6使用变量名进行计算
a=10
b=11
c=660
d=c/b/a
print("这是一个变量名计算,其结果为：",d)




