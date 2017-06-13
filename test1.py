# -*- coding： utf-8 -*-

#List
# use list
classmates = ['Michael', 'Bob', 'Tracy']

classmates[0]
classmates[1]
classmates[2]

# get the last element of list
classmates[-1]
# get the last tow element of list
classmates[-2]
#....

#add new elements  to the list
classmates.append('Adam')

#add new element to a certain position
classmates.insert(2, 'Jack')

#delete the last elemnet
classmates.pop()

#delete a element in a certain position
classmates.pop(1)

# So, list 用的是堆，LIFO, 在list 的最后面进行操作，先入先出

#替换某个元素可以直接用赋值

#list里面的元素支持不同的类型

#list元素也可以是另外一个list
s = ['python', 'java', ['asp', 'php'], 'basic']
#所以该list是二维的
#拿到二维元素可以用
s[2][1]

#list 可以为空


#------------------------------------------

#Tuple  元组

# use tuple
classmates = ('Micjael', 'Bob', 'Tracy')
# tuple 和 list很类似， 但是是静态的

#如果要定义一个空的tuple
t = 0
# 其实就是一个 int 吧。。。

#定义一个一个数的tuple
t = (1,)
#加 ‘，’ 以对数学符号 括号 加以区分

# tuple 可以包含  list  这时可以把该 tuple 看成是可变的，但其实可变的是 tuple 里面的 List
t = ('a', 'b', ['B', 'c'], 'c')
#这同样也是一个二维的 tuple 
#对二维 tuple 的操作同 list 一样



#--------------------------------------------

#条件判断

age = 3
if age >= 18:
	print("your age is ", age)
	print("adult")
else:
	print("your age is ", age)
	print("reenager")

#使用 elif , elif == else if 
 if age >= 18:
 	print("your age is ", age)
 	print("adult")
 elif age >= 12:
 	print("teenager")
 else:
 	print("kid")
#

if x:
	print("True")
#

int birth = input("birth: ")
if birth < 2000:
	print("前")
else:
	print("后")


#----------------------------------------
# 循环 loop

# for loop
# form 1
name = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)

# form 2
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)

# form 3 -- use range()
sum = 0
for x in range(1000):
	sum = sum + x
print(sum)

# while loop

sum = 0
n = 100
while n > 1:
	sum = sum + n
	n = n // 2
print(sum)


# with ' break '
n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END')

# with ' continue '
n = 0
while n <= 100:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)



#-----------------------------------------
#Use dict (dictionary)--( key -value )
d = {'Micheal': 95, 'Bob': 80, 'Tracy': 90}
d['Michael']
# This can directly find and print out Micheal's grade

# you can also put elements by key
d = ['Adam'] = 67
d['Adam']

# you can judge if such en element exists
'Thomas' in d
# it will return true or false

# get

d.get('Thomas')
d.get('Thomas', -1)

# delete elements from a dict
d.pop('Bob')

# 和list比较，dict有以下几个特点：
# 1. 查找和插入的速度极快，不会随着key的增加而变慢；
# 2. 需要占用大量的内存，内存浪费多。

# 而list相反：
# 1. 查找和插入的时间随着元素的增加而增加；
# 2. 占用空间小，浪费内存很少。

# dict 用的是 Hash 哈希算法

#-----------------------------------------------
#	Use set

s = set([1, 2, 3])
# use key should with list's help

# add elements to the set
s.add(4)

# set can not have some elements
# if you the add elements have already exits, in will be automatically ignored

# remove the elements

s.remove(4)
# sets can be combined with each other
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

s1 & s2 == {2, 3}
s1 | s2 == {1, 2, 3, 4}

# list +

a = ['c', 'b', 'a']
a.sort() == ['a', 'b', 'c']

# str +

a = 'abc'
a.replace('a', 'A')
# a still == 'abc', because str can not change, a just point at 'abc'
# but 

a = 'abc'
b = a.replace('a', 'A')

#now
b == 'Abc'
#but
a == 'abc'
