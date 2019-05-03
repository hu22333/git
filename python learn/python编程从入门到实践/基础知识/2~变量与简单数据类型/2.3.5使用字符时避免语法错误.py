#在使用单引号括起的字符串中包含撇号，会导致错误
message="one of Python's strength is its diverse community."
print(message)#撇号位于双引号之间，因此正确
#错误用法
message='one of Python's strength is its diverse community.'
print(message)
