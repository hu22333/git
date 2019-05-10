# ex6.py
# 变量types_of_people赋值为10
types_of_people = 10
# 将变量There are {types_of_people} types of people.赋值给x,其中types_of_people变量的值为10
x = f"There are {types_of_people} types of people."  # 第一处
# binary赋值给binary变量
binary = "binary"
# don't赋值给do_not变量
do_not = "don't"
# 将变量。。。赋值给y,其中binary变量的值为binary，do_not变量的值为don't"
y = f"Those who know {binary} and those who {do_not}."  # 第二处
# 打印x与y
print(x)
print(y)
# 打印I said加变量x的值，与I also said加变量y的值
print(f"I said:{x}")  # 第三处
print(f"I also said: '{y}'")  # 第四处
# False赋值给hilarious
hilarious = "False"
# Isn't that joke so funny?！{}赋值给joke_evaluation
joke_evaluation = "Isn't that joke so funny?！{}"
# 打印joke_evaluation并在括号内填充hilarious变量，其中.format（）是为了使字符串类型格式化
print(joke_evaluation.format(hilarious))
# 。。。赋值给w，。。。赋值给e
w = "This is the left side of..."
e = "a string with a right side"
# 合并打印
print(w+e)
