# list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']  # 元素由0开始计数到2，范围为len(classmates）-1
print(len(classmates))  # list元素的个数
print(classmates)
print(classmates[0])
# 可按倒数的来算
print(classmates[-1])
# ist是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)
# 元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)
# 删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
# 没有append()，insert()这样的方法，可以正常地使用classmates[0]，classmates[-1]
classmates = ('Michael', 'Bob', 'Tracy')  # 括号不一样list是[]
