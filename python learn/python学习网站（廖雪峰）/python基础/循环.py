#循环分为两种
#for ....   in
#以及while
#元素迭代出来
name=['M','B','T']
for name in name:
    print(name)
#累加
sum=0
for x in[1,2,3,4,5,6,7,8,10]:
    sum=sum+x
print(sum)
#python提供range()函数,可生成一个整数数列
print(list(range(5)))
#生成0-100累加
sum=0
for x in range(10):
    sum=sum+x
print(sum)
#注：若print在for内则打印数组sum是变化的，而不是最终值
sum=0
for x in range(101):
    sum=sum+x
    print(sum)
#while循环（设置n）
a=0
n=99
while n>0:
    a=a+n
    n=n-2
print(a)
#练习
L=['Bart','Lisa','Adam']
for L in L:
    print('hello,',L)
