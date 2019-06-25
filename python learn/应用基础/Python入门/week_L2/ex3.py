# 分支循环操作小练习
if 0:
    print("Hello")
if 1:
    print("hello")

if "":
    print("Hello")
if []:
    print("Hello")
if {}:
    print("Hello")
if "Not Empty":
    print("Hello")

if [10, "101"]:
    print("hello")
if True:
    print("Hello")
if False:
    print("Hello")
if 0 == 1:
    print("hello")

a = 10
if a > 10 or a < 10:
    print("a is not 10")
else:
    print("a is 10")

a is 10
if a > 10:
    print("a>10")
elif a < 10:
    print("a<10")
else:
    print("a=10")

a = 10
print(range(10))
print(list(range(10)))

for i in range(10):
    print(i, end="")

for i in [0, 1, 2, 3, 4]:
    print(i, end="")

for i in range(1, 10, 2):
    print(i, end="")

print(list(range(1, 10, 2)))

for c in "Python语言":
    print(c)
for c in "Python语言":
    print(c, end=",")

while a > 5:
    print(a)
    a = a-1

while False:
    print("Hello")
while True:
    print("Hello")
    break

print(a)
while a > 0:
    a = a - 1
    if a % 2 == 0:
        continue
    print(a)

try:
    a=10/0
except:
    print("error")

try:
    a=oprn("no-exist")
except:
    print("error")

try:
    if x:
        print("Hello")
except:
        print("error")
try:
    anyerror
except:
    print("error")


