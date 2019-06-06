#ex15.py
#从软件包sys中取出argv（参数变量）这个特性
from sys import argv
#解包，参数需用户执行命令时依次赋值
script,filename=argv
#open() 函数用于打开一个文件，创建一个file对象，并进行变量的赋值
txt=open(filename)
#打印字符串，且{filename}为格式化字符串，将filename变量的值赋值给{filename}
print(f"Here's your file {filename}:")
#读取txt文本，文件从open处获取的文件
print(txt.read())
#直接打印
print("Type the filename again:")
#输入命令前加修改提示符
file_again = input("> ")
#打开文件，变量赋值
txt_again=open(file_again)
#读取
print(txt_again.read())