# 多数列表都是动态的，列表创建后，将随程序的运行增删元素
# 3.2.1 修改列表元素
# 修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2在列表中添加元素
# 1 在列表末尾添加元素[使用append()]
# 例1
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
# 例2
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# 2 在列表中插入元素[使用insert()]
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')  # 在0索引处添加
print(motorcycles)

# 3.2.3 从列表中删除元素
# 方法一(del语句)，可删除任意位置的列表元素，，条件是知道其索引
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
# 方法二(pop()),可删除列表末尾的元素，并接着使用它的值。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()  # 未填索引默认为末尾
print(motorcycles)
print(popped_motorcycle)
# 使用pop()删除任意位置的元素并使用
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(motorcycles)
print('The first motorcycle I owned was a ' +
      first_owned.title()+'.')  # title中文：标题，表示首字母大写

# 根据值删除元素(使用remove())
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# 使用remove()从列表删除元素，也可以使用其值(注意remove()只删除第一个指定的值)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")

# 练习
# 3-4嘉宾名单
name = ['Mrs Zhang', 'Mrs Cao', 'Mr Hu']
print(name)
# 3-5修改嘉宾名单
name = ['Mrs Zhang', 'Mrs Cao', 'Mr Hu']
absent_name = name.pop(0)
print(absent_name, 'can not go to party')
name.append('Mr Qu')
print(name)
print('hello', name[0], 'welcome to this meetting')
print('hello', name[1], 'welcome to this meetting')
print('hello', name[2], 'welcome to this meetting')
# 3-6添加嘉宾
print('we find a big table')
name = ['Mrs Zhang', 'Mrs Cao', 'Mr Hu']
name.insert(0, 'Mr Xie')
name.insert(2, 'Mr Zhu')
name.append('Mr Liu')
print('hello', name[0], 'welcome to this meetting')
print('hello', name[1], 'welcome to this meetting')
print('hello', name[2], 'welcome to this meetting')
# 3-7缩减名单
name = ['Mrs Zhang', 'Mrs Cao', 'Mr Hu', 'Mr Xie', 'Mr Liu']
print(name)
print('sorry,we can go home,and I need two people')
now_name = name.pop(0)
print(now_name, ', sorry,you can not go to this meet')
now_name = name.pop(0)
print(now_name, ', sorry,you can not go to this meet')
now_name = name.pop(0)
print(now_name, ', sorry,you can not go to this meet')
print(name)
print(name[0], ', you can go to this meet')
print(name[1], ', you can go to this meet')
print(name)
del name[0]
del name[0]
print(name)
