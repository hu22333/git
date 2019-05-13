#脚本添加参数，自己设置参数
from sys import argv

Script,name,number,hehe=argv
a='> '
print(f"Who are you?I'm {name}.I'm the{Script}.")
print(f"How many people are there in the room now?{number}. ")
print(f"胡子轩有几个女朋友?{hehe}")
print(f"Ask a few questions now.")

print('number?')
b=input(a)
print('Who?')
c=input(a)
print('food？')
d=input(a)
print(f"""like {b},like {c},like {d}""")

