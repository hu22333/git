#ord()函数获取字符的整数表示
#chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(65))
print('\u4e2d\u6587')
#格式化
#%s表示用字符串替换，%d表示用整数替换
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
#占位符 %d整数，%f浮点数，%s字符串，%x十六进制整数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print( 'growth rate: %d %%' % 7)
#使用format()格式化字符串
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
#练习
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1=72
s2=85
r=(85-72)/72*100
print('{0}分数提高了{1:.1f}%'.format('小明',r))

