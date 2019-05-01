# dict全称dictionary(字典),也称map,使用健-值（key-value）存储
# 举例子，查成绩需要两个list，有序集合
# name=['Michael','Bob','Tracy']
# scores=[95,75,85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85,'Adam':67}
print(d['Michael'])
print(d['Adam'])
#避免key不存在的错误，使用in判断key是否存在
print('Adam' in d)
#删除一个Key,用pop(key)的方法，对应的value也会从dict种删除
d.pop('Bob')
print(d)

#set也是一组key的集合，但不存储value（key不能重复，重复会被自动过滤）
s=set([1,2,3])
print(s)
s=set([1,1,2,2,3,3,3,4,4,])
print(s)
#通过add(key)添加元素
s.add(5)
print(s)
#通过remove(key)方法删除元素
s.remove(1)
print(s)
#set可以看作数学意义上的无序和无重复元素的集合，可以做数学意义的交集，并集等操作
s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)
#注意：
#list为可变对象，str是不变对象
a=['c','b','a'] #可变
a.sort()
print(a)

a='abc' #不可变
a.replace('a','A')
print(a)
#区分a,b都是变量
a='abc'
b=a.replace('a','A')
print(a)
print(b)
#总结：对于不变对象，调用对象自身的任意方法，也不会改变该对象自身的内容。





