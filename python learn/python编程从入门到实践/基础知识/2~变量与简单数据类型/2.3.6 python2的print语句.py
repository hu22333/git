#python2中print无需把打印的内容放在括号当中
print  "hello Python 2.7 world!"

#练习
#2-3个性化消息
massage='hello Eric, would you like to learn some Python today?'
print(massage)

#2-4调整名字大小写
name='Hu Zixuan'
print(name.upper())
print(name.lower())
print(name.title())

#2-5名言
print('Shakespeare once said,"To be or not to be, that is a question".')
#2-6名言2
message='Shakespeare once said,"To be or not to be, that is a question".'
print(message)
#2-7剔除人名中的空白
a=' python '
b='learn'
print(a.lstrip()+b)#删前
print(a.rstrip()+b)#删后
print(a.strip()+b)#删前后
