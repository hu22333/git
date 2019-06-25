# 数值计算综合练习
print(10+12.3)
print(0xa+0b1010)
print(int(1.99))  # 取整
print(round(1.99))  # 四舍五入
print(float(10))  # 变浮点
print(complex(10))  # 变复数
print(type((10+0j).real))  # 类型
print((1+2j)*0)  # 复数运算
print(1.23*0)
print(1024*0)
print(abs(3+4j))
print(str(3+4j))
print(hex(123))  # 整数变八进制

a = 2**10
b = 1+2j
a, b = b, a  # 互换a=b,b=a
print(a, b)
a *= 0
print(a)
print(int(a))
print(int(a.imag))
print(max(1, 1.0, 0.4))
print(max(1.0, 1, 0.4))
print(min(1, 1.0, 1))
type(100//11)
type(100/11)
print(type(100 % 2.0) == type(1))
print(len(str(999**99))  # str输出字符串，len为返回字符串长度

#
a=12356
b=a**789
print(len(str(b)))
