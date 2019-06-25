#字符串操作小练习
print("python")
print('python')
print('Python'=='python')
print('Python'=='Python')#大小写影响
print("Python"[0])#字符串索引
print("Python"[-1])
s="Python是一门好语言"
print(s)
print(type(s))#类型
print(len(s))#长度
print(s[-2:-1])#切片
print(s[1:3])
print(s[:3])
print(s[-2:])
print(s[:])
print(s.split('是'))
t="Python 是 一门 好语言"
print(t.split())
print("Python","C")
print(s)
print(t)
print(s.replace("Python","C"))
print(t)
print(s*2)
print(s)
print(2*s)
print(s+t)
print("python"in s)
print("C" not in s)
print("{}是一门好语言".format("Python"))
print("{}是一门好{}".format("Python","语言"))
print("{}".format(s))
print("{:.2}".format(s))
print("{:.6}".format(s))
