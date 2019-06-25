# 传感器日志输出
f = open('C:\\Users\\hu\\git\\ex\\sensor-data-1k.txt', 'r')  # 打开文件
count = 0  # 计数
for line in f:
    count += 1
    if count % 100 == 0:
        print(line, end="")  # end=""添加一个空字符，则print函数不会在字符串末尾添加一个换行符
f.close()  # 关闭文件

# 循环内还是外的例子
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
    print(sum)  # 逐行循环内

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)  # 最终值循环外
