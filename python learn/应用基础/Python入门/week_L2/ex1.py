#数值计算小练习
a = 0xa+0b1010+12.34
b = int(11.99)
print(a,b)
a,b = b,a
print(a,b)
a = -a
b = complex(b)
print(a,b)
print(a+b)
print(a+b==21.34+0j)
print(a+b==21.340000000000003)
print(round((a+b).real,2)==21.34)#四舍五入，实部，保留后两位
print(hex(425))#整数变十六进制
print(max(0x1a9,425,400))
print(425/125)

#
a = 123.456
b = 456.789
print(round(a+b, 3) == 580.245)
