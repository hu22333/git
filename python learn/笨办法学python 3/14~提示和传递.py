# ex14.py为原代码,运行的时候在ex文件夹
# ex14_1.py修改提示符
# ex14_2添加一个参数（其中添加一个参数的话，运行Windows PowerShell需要多输出一个命令）

from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name},I'm the {script}.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Aliright,so you said {likes} about liking me.
You live in {lives}.Not sure where that is.
And you have a {computer} computer. Nice.
""")
