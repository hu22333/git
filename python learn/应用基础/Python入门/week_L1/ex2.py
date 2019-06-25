# 浮点数计算
print(12.3+98.7)
print(1.23e1+9.87e1)
print(type(12.3))  # 类型
print(type(123))  # 类型
print(str(12.3))  # 值转字符串
print(float(123))  # 将整数和字符串转换成浮点数
print(float("12.3"))  # 将整数和字符串转换成浮点数
a = 101
b = 1.0
print(a*b)
print(12.3*0.1)
print(round(0.1+0.2, 1))  # 按照指定的小数位数进行四舍五入运算
print(0.1+0.2 == 0.3)  # 判断
print(round(0.1+0.2, 1) == 0.3)  # 按照指定的小数位数进行四舍五入运算
print("{:.2f}".format(1234.56789))  # 浮点后2位
print("{:.1f}".format(1234.56789))  # 浮点后1位
print("{:.10f}".format(1234.56789))  # 浮点后10位
print("{:,.1f}".format(1234.56789))  # 浮点
print("{:.1e}".format(1234.56789))  # 科学计数
print(min(1.23, 4.56, 1, 1.1))
print(max(1.23, 4.56))
print(pow(1.23, 4.56))

a = 12.3
b = 45.6
if round(a + b, 1) == 57.9:
    print("equal")
else:
    print("not equal")
