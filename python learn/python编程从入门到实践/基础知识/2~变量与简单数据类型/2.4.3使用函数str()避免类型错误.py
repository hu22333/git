#类型错误，系统不知道如何解读这个整数变量（int）
age=23
message="happy "+age+"rd Birthday"
print(message)
#使用调用函数str()，使非字符串值表示为字符串
age=23
message="happy "+str(age)+"rd Birthday"
print(message)
# python2中3/2返回的结果为1，整数除法只会包含整数部分
#小数部分会被直接删除，若要避免使用3.0/2

#试一试
#2-8数字8
print(5+3)
print(10-2)
print(2*4)
print(80/10)
#2-9最喜欢的数字
a=520
print("我最喜欢的数字是"+str(a))

