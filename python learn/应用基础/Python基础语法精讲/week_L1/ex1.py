# 字符串之基本操作小练习
a = "PYPY"
b = '语言'
print(a+b)  # 字符串合并
print(a, b)  # 分别打印
a += b  # a=a+b
print(a)
print(a[4:0])  # 切片从4索引开始
print(a[:-1:2])  # 0开始-1截至，间隔长度为2（0，2，4）
print(a[::-1])  # 反转
print(a[::-2])  # 反转，且间隔长度为2
print(a[::])
print("Py" in a) #判断是否在列表中
print("Py" not in a) #判断是否不在列表中
print("PY" in a) 
print(b in a) #由a=a+b，故显示True
print(a*3) 
print(a*0)
print(a*-2)
c = "\'\"\\{\}\*" #"  "内部保留，外""消失，\为转义字符串，之后符号保留,\\表反斜杠\
print(c)
print(c+"\t\\") #\t表TAB，\\表反斜杠\
#例子
a = "Python基础语法\n精讲" #[M:N:K],M缺失默认为至开头，N缺失默认为至结尾
print(a[:-2]) #0到-2
print(a[-3::]*2) 
print("\n精讲\n精讲")