#字符串之函数小练习
print(len("PYPY123")) #len()函数可返回字符串的长度
print(len("中West文混合"))
print(str(123)) #str()返回字符串形式
print(str(123.456))
print(chr(1234)) #1234为Unicode编码，返回其对应的字符
print(chr(4321))
print(chr(65))
print(ord('a')) #a为字符，返回对应Unicode编码
print(ord('好'))
print(ord('和'))
print(ord('和')+ord('平'))
print(hex(1234)) #整数变十六进制
print(oct(1234)) #整数变八进制
print(bin(1234)) #bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
print(hex(-1234))
print(oct(-1234))
print(bin(-1234))
print(bin(-0))
print(hex(True))
print(hex(False))
#例子
for c in "Python字符串":
    print(ord(c), end=",")#P，y,....对应的Unicode码
print("\n")
print(ord("P")) #如例子所示
print(ord("y")) #