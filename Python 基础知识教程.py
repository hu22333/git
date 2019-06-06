#列表和循环
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
#for dog in dogs:关键词 “for” 代表着循环的开始。变量 “dog” 是一个临时占位符变量。Python 会把每一项放进这个占位符变量，一次一个。第一次循环，“dog” 的值为 “border collie”，依次类推。
#当列表中没有元素可以访问，循环结束
for dog in dogs:
    print(dog)
#穷举列表:循环一个列表的时候，你可能想获取当前元素的索引。你可以采用 list.index(value) 的方式获取，
#或者采取一个更简单的方法。enumerate() 函数可以帮助你跟踪每项元素的索引，

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print("Resultes for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index)
    print("Place: " + place + " Dog: " + dog.title())
#枚举一个列表，需要添加一个 index 变量存储当前元素的索引。因此循环语句边为：
#for index, dog in enumerate(dogs)
#index 值的类型为整型，如果你想以字符串的形式打印，你需要用 str(index) 将 index 转换成字符串。'''

#For循环
#For 循环
#for 循环语句是 Python 中常用的迭代机制。
#Python 中几乎所有的数据结构都可以用 for 来迭代。 列表，元组，字典等等
#也可以用 while 代替 for 循环。
#for 循环中特殊的关键字
#Python 的 for 循环中有两个特殊关键字：break，continue

#Break 用来立即终止循环并退出。
#Continue 用来跳出当前迭代进入下一个迭代。
#Note: 这两个关键字也可以用在 while 循环中。'''


#列表常用操作
#1 修改元素：知道元素的位置，可以更改元素的值
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs[0] = 'australian shepherd'
print(dogs)

#2 查找元素：如果要定位列表中的元素，可以使用 index() 函数
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
print(dogs.index('australian cattle dog'))

#3 检测元素是否在列表中:关键字 in 用来检测元素是否在列表中。
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
print('australian cattle dog' in dogs)
print('poodle' in dogs)

#4 添加元素:
#(1)在列表尾部添加元素:append() 函数在列表尾部添加元素。
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.append('poodle')
for dog in dogs:
    print(dog.title() + "s are cool.")

#(2)向列表中插入元素:insert() 函数可以插入到任意位置。指定一个位置插入元素，这个位置之后的所有元素的索引都增加1。
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.insert(1, 'poodle')
print(dogs)

#(3)创建空的列表:了解到列表的添加操作后，我们可以动态的利用列表。不再局限于固定的定义整个列表。
# 一个常见的动态利用列表的方法是定义一个空的列表，动态的添加元素。例如：构建一个网站，网站的用户可以用列表来定义，开始一个空列表，随着用户数的增加，不断扩大列表。
# Create an empty list to hold our users.
usernames = []
# Add some users.
usernames.append('bernice')
usernames.append('cody')
usernames.append('aaron')
# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')
#如果我们不打乱列表的顺序，可以用列表找出最新和最老的用户
# Create an empty list to hold our users.
usernames = []
# Add some users.
usernames.append('bernice')
usernames.append('cody')
usernames.append('aaron')
# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')
# Recognize our first user, and welcome our newest user.
print("\nThank you for being our very first user, " + usernames[0].title() + '!')
print("And a warm welcome to our newest user, " + usernames[-1].title() + '!')

#列表排序:可以按照字母序排序，或者相反的方向
students = ['bernice', 'aaron', 'cody']
# Put students in alphabetical order.
students.sort()
# Display the list in its current order.
print("Our students are currently in alphabetical order.")
for student in students:
    print(student.title())
#Put students in reverse alphabetical order.
students.sort(reverse=True)
# Display the list in its current order.
print("\nOur students are now in reverse alphabetical order.")
for student in students:
    print(student.title())
#sorted() vs sort():sort() 函数排序过后，原列表已经发生了变化。如果想保留原列表，生成一个新的列表，可以使用 sorted() 函数
students = ['bernice', 'aaron', 'cody']
# Display students in alphabetical order, but keep the original order.
print("Here is the list in alphabetical order:")
for student in sorted(students):
    print(student.title())
# Display students in reverse alphabetical order, but keep the original order.
print("\nHere is the list in reverse alphabetical order:")
for student in sorted(students, reverse=True):
    print(student.title())
print("\nHere is the list in its original order:")
# Show that the list is still in its original order.
for student in students:
    print(student.title())

#反转列表:就是反转的初始顺序。reverse() 函数实现了这一功能
students = ['bernice', 'aaron', 'cody']
students.reverse()
print(students)

#排序数值列表
numbers = [1, 3, 4, 2]
# sort() puts numbers in increasing order.
numbers.sort()
print(numbers)
# sort(reverse=True) puts numbers in decreasing order.
numbers.sort(reverse=True)
print(numbers)
numbers = [1, 3, 4, 2]
# sorted() preserves the original order of the list:
print(sorted(numbers))
print(numbers)
numbers = [1, 3, 4, 2]
# The reverse() function also works for numerical lists.
numbers.reverse()
print(numbers)

#列表长度:len() 函数用来获取列表长度
usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)
print(user_count)

#列表通过位置移除元素：知道元素位置的前提下，可以通过 del 语句删除列表元素。
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove the first dog from the list.
del dogs[0]
print(dogs)

#通过值移除元素：remove() 函数可以通过元素的值来移除元素。给定元素值和要删除的列表名，Python 会搜索给定列表，直到找到第一个和给定值相同的元素，然后移除元素
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove australian cattle dog from the list.
dogs.remove('australian cattle dog')
print(dogs)
#注意：只有找到的第一个元素会被移除，当有多个相同值的元素时，剩下的元素不会被移除。
letters = ['a', 'b', 'c', 'a', 'b', 'c']
# Remove the letter a from the list.
letters.remove('a')
print(letters)

#从列表中 popping 元素：
#在程序设计中有一个很有意思的概念：从集合中 'popping' 元素。每一种程序设计语言都有类似 Python 中列表的数据结构。所有这些结构都可以用作队列。处理队列元素的方法也是多种多样。
#其中一个简单的方法是，开始创建一个空列表，不断的增添元素。当需要取出元素时，总是从最后一个元素开始，取出后再从列表中移除。pop() 函数就是来处理这种操作的
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
last_dog = dogs.pop()
print(last_dog)
print(dogs)
#这种操作也叫做先进后出的操作。最先进入列表的元素总是最后一个取出的。
#事实上，你可以利用 pop() 函数处理任意的元素。只要给出想要 pop 出去的元素的索引。因此我们也可以作先进先出的操作。
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
first_dog = dogs.pop(0)
print(first_dog)
print(dogs)

#Python 基础知识教程-列表切割操作
#列表是一系列元素的集合，我们应该能够获得集合的任意子集。对列表来说，我们应该能够获取列表的前3个，后3个，中间的任意3个连续的列表子集。这种获取任意 x 个连续列表元素的操作称之为切割（slices）。
#为了获取到我们想得到的列表子集，我们应当给出子集中第一个想要的元素的位置和第一个不想要的元素的位置。因此 list[0 : 3] 会包含列表中元素 0，1和2，但不包括 3（数字代表索引）。
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
# Grab the first three users in the list.
first_batch = usernames[0:3]
for user in first_batch:
    print(user.title())
#如果你想获取指定位置之前的所有元素，可以置空冒号前的第一个索引
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
# Grab the first three users in the list.
first_batch = usernames[:3]
for user in first_batch:
    print(user.title())
#从列表中切割后，原列表不受影响
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
# Grab the first three users in the list.
first_batch = usernames[0:3]
# The original list is unaffected.
for user in usernames:
    print(user.title())
#我们可以获取列表中任意元素段
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
# Grab a batch from the middle of the list.
middle_batch = usernames[1:4]
for user in middle_batch:
    print(user.title())
#如果你想获取指定位置之后的所有元素，可以置空冒号后的索引
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
# Grab all users from the third to the end.
end_batch = usernames[2:]
for user in end_batch:
    print(user.title())

#复制一个列表
#利用切割操作可以复制一个列表，只需要置空冒号前后的索引
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
# Make a copy of the list.
copied_usernames = usernames[:]
print("The full copied list:\n\t", copied_usernames)
# Remove the first two users from the copied list.
del copied_usernames[0]
del copied_usernames[0]
print("\nTwo users removed from copied list:\n\t", copied_usernames)
# The original list is unaffected.
print("\nThe original list:\n\t", usernames)

#Python 基础知识教程-数字列表
#range()函数：普通的列表创建方式创建10个数是可以的，但是如果想创建大量的数字，这种方法就不合适了。range() 函数就是帮助我们生成大量数字的。
# print the first ten number
for number in range(1, 11):
    print(number)
#range() 函数的参数中包含开始数字和结束数字。得到的数字列表中包含开始数字但不包含结束数字。同时你也可以添加一个 step 参数，告诉 range() 函数取数的间隔是多大。
# Print the first ten odd numbers.
for number in range(1,21,2):
    print(number)
#如果你想让 range() 函数获得的数字转换为列表，可以使用 list() 函数转换。
# create a list of the first ten numbers.
numbers = list(range(1,11))
print(numbers)
#这个方法是相当强大的。现在我们可以创建一个包含前一百万个数字的列表，就跟创建前10个数字的列表一样简单。
# Store the first million numbers in a list
numbers = list(range(1,1000001))
# Show the length of the list
print("The list 'numbers' has " + str(len(numbers)) + " numbers in it.")
# Show the last ten numbers.
print("\nThe last ten numbers in the list are:")
for number in numbers[-10:]:
    print(number)

#min(),max()和sum()函数：你可以将这三个函数用到数字列表中。min() 函数求列表中的最小值，max() 函数求最大值，sum() 函数计算列表中所有数字之和。
ages = [23, 16, 14, 28, 19, 11, 38]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)
print("Our youngest reader is " + str(youngest) + " years old.")
print("Our oldest reader is " + str(oldest) + " years old.")
print("Together, we have " + str(total_years) + 
      " years worth of life experience.")


#Python 基础知识教程-列表推导式
#数字列表的推导式
# Store the first ten square numbers in a list.
# Make an empty list that will hold our square numbers.
squares = []
# Go through the first ten numbers, square them, and add them to our list.
for number in range(1,11):
    new_square = number**2 #乘方
    squares.append(new_square)
# Show that our list is correct.
for square in squares:
    print(square)
#上述代码中我们实现了创建包含10个数字的列表，对每个数字作平方操作并将它们存储进新的数组的功能。代码略显冗长，我们可以省略 for 循环中的 new_square 参数，简化代码。使用列表推导式就可以进一步简化代码，
# Store the first ten square numbers in a list.
squares = [number**2 for number in range(1,11)]
# Show that our list is correct.
for square in squares:
    print(square)
#首先我们定义了一个列表，名字为 squares 。
#接下来看看列表中括号中的代码：
#for number in range(1, 11)
#它在1-10之间创建一个循环，把每个数字存储到变量 number 中。接下来我们看一看对每次循环中的 number 作了哪些操作。
#number**2
#每个 number 都作了平方操作，并将结果存储在了定义好的队列中。我们可以用如下语言来阅读这行代码：
#squares = [raise number to the second power, for each number in the range 1-10]、

#其他例子
#上个例子是对数字作平方操作，下列代码是对数字作乘操作，仔细阅读代码，体会数字列表表达式的用法
# Make an empty list that will hold the even numbers.
evens = []
# Loop through the numbers 1-10, double each one, and add it to our list.
for number in range(1,11):
    evens.append(number*2)  
# Show that our list is correct:
for even in evens:
    print(even)
#简化后
# Make a list of the first ten even numbers.
evens = [number*2 for number in range(1,11)]
for even in evens:
    print(even)

#非数字列表的推导式
#我们也可以在非数字列表中运用推导式。在下面的例子中，我们会创建一个非数字列表，然后利用推导式生成一个新的列表。不运用推导式的源代码如下所示：
# Consider some students.
students = ['bernice', 'aaron', 'cody']
# Let's turn them into great students.
great_students = []
for student in students:
    great_students.append(student.title() + " the great!")
# Let's greet each great student.
for great_student in great_students:
    print("Hello, " + great_student)

#我们想写下如下所示的推导式：
#great_students = [add 'the great' to each student, for each student in the list of students]
# Consider some students.
students = ['bernice', 'aaron', 'cody']
# Let's turn them into great students.
great_students = [student.title() + " the great!" for student in students]
# Let's greet each great student.
for great_student in great_students:
    print("Hello, " + great_student)
