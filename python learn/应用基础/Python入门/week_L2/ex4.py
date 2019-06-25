# 列表操作小练习
print([])
print([1, 2, "1", "2"])
ls = [1, 2, "1", "2", [1, 2, 3, 4]]
print(ls[0])
print(ls[-1])
print(ls[-1][-1])
print(ls[0:3])
print(ls[-4:-1])
print(ls*2)
ls.append(5)  # 末尾加元素
print(ls)
ls.remove(ls[-1])  # 移除最后一位
print(ls)
print(len(ls))  # 列表长度
del ls[3]  # 删除索引位置3，及0，1，2，3属于第四位
print(ls)
ls[::-1]  # 位置翻转
print(ls)
ls.clear()  # 清除数据
print(ls)

# 例子
ls = list(range(1, 11))  # 列表1到11，即[1,2,...11]
sum = 0
for i in ls:
    sum += i  # 累加0+1+2...+11=11*5=55
print(sum)
