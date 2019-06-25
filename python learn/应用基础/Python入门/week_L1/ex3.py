# 复数计算练习
print(12+34.5j)
print(12+34.5j+6+7.8j)
print(type(1+2j))
complex(123)#创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数
print((1+2j)**10)
print((1+2j)**2)
z = 12+34.5j
print(z)
print(z.imag)#虚部
print(z.real)#实部
print(type(z.imag))
print(type(z.real))
y = 1+2j
print(y*z)
print(1+2j == 1.0+2.0j)#判断

#判断复数运算的类型(已更改)
z = 12.3 + 45.6J
y = 12.3 - 45.6j
print(z*y)
print(type(z*y))#复数
print(type(1j))#复数
print(type(1))#整数
print(type(1.0))#浮点
if type(z*y) == type(1j):
    print("complex")
elif type(z*y) == type(1):
    print("int")
elif type (z*y) == type(1.0):
    print("float")
else:
    print("others")
