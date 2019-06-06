#ex15_4.py为删除10~15行的代码
from sys import argv
script,filename=argv
txt=open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
