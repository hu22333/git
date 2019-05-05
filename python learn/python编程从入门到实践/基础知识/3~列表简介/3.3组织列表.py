# 3.3.1使用方法sort()对列表进行排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
car.sort()  # 按照字母顺序排列
print(cars)
b_cars = ['bmw', 'audi', 'toyota', 'subaru']
b_cars.sort(reverse=True)  # 按照字母顺序相反排列
print(b_cars)

# 3.3.2使用函数sorted()对列表进行临时排序(并不改变列表元素顺序)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the orignal list again:")
print(cars)
# 3.3.3倒着打印列表(反转列表元素顺序使用reverse)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # 永久修改列表元素，但再次reverse()可以恢复
print(cars)
# 3.3.4确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

# 练习
# 3-8放眼世界
place = ['北极', '青藏', '东京', '香港']
print(place)
print(sorted(place))
print(sorted(place, reverse=True))  # 注意用法
print(place)
place.reverse()  # 反转
print(place)
place.reverse()  # 恢复原始
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)
