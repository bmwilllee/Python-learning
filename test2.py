# 函数调用

# 以圆心面积计算公式为例
s = area_of_circle(x)

# python 函数库 http://docs.python.org/3/library/functions.html#abs

# abs() 用于计算绝对值
abs()

# max() 可以接受任意多个参数，并返回最大的那个
max(1,2,3,4,5,6,7,8,9,10) == 10

# 数据类型转换函数
int()
float()
str()
bool()
#.....

# python 甚至可以将函数名赋给一个变量， 其实就是给这个函数起了一个别名
a = abs
a(-1)
#可以返回 -1 的绝对值

# 进制转换函数
hex()
oct()
bin()


#---------------------------------------------------

# 自定义函数

# 用 def 语句来定义函数
# 以求绝对值的自定义函数 my_abs 为例
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

# 你可以定义多个函数，然后保存在一个文件当中， 在python 交互里面
# 用 form + fileName(不包含后缀) + import + functionName 来导入 funtions


# 空函数， 在没有想好函数的用途的时候，定义一个空函数也是可以的，可以保证不影响代码的运行
 def nop():
 	pass

 	# pass 也可以用在其他语句当中，例如
 	if age >= 18:
 		pass

 # 对 my_abs() 的完善，使其具有参数（operand）的检查报错

 def am_abs(x):
 	if not isinstance(x, (int, float)):
 		raise TypeError('bad operand type for my_abs()')
 	if X >= 0:
 		return x
 	else:
 		return -x

 # 函数返回多个值

 import math
# 可以引入包，获得包内的方法
 def move(x, y, step, angle = 0):
 	nx = x + step * math.cos(angle)
 	ny = y - step * math.sin(angle)
 	return nx, ny

r = move(100, 100, 60, math.pi / 6)
# pi 指的是 180°
# 返回的是一个包含多个值的 tuple 

# 练习

import math

def quadratic(a, b, c):
	for x in [a, b, c]:
		if not isinstance(x, (int, float)):
			raise TypeError('bad operand type : ', x)
	i = b*b*4*a*c
	if m < 0:
		return ' this input funcion has no solution'
	elif m = 0:
		x1 = x2 = -(b / (2*a))
		print('This given function has two same solutions：')
	else:
		x1 = (-b + math.sqrt(m)) / 2*a
		x2 = (-b - math.sqrt(m)) / 2*a
	return x1, x2



#----------------------------------------------------------------------
#函数的参数

def power(x, e):
	s = 1
	while e > 0:
		e = e-1
		s = s * s
	return s

#python 支持默认参数
# 比如 power = 2 是我们经常需要计算的量， 那么我们可以社 e 的默认值为2
# 这样在计算平方的时候，秩序要传一个参数就可以完成 power(5) = 25

def power(x, e=2):
	s = 1
	while e > 0:
		e--
		s = s * s
	return s

# 在使用默认参数时，确保
# 1. 默认项在确定项的后面，否则编译器会出错
# 2. 当函数由多个参数时，把变化大的参数放在前面，变化小的放在后面，变化小的就可以作为默认参数

# 使用默认参数可以降低调用函数的复杂度

def enroll(name, gender, age=6, city='Beijing'):
	print(name)
	print(gender)
	print(age)
	print(city)

# 可以不按照参数的顺序来给参数赋值，但是需要把参数名给附上
#比如
enroll("Adam", 'M', city = "Tianjin")


# 来看下面这个例子，是在使用默认参数的时候可能回遇到的问题
def add_end(L = []):
	L.append('END')
	return L
#这个函数在调用的时候，会遇到这样的问题
add_end()
#当我们在使用默认参数的时候，第一次调用之后，再调用一次默认参数的话
add_end()
# L 就会有两个 END


# 所以，定义默认参数时，默认参数一定要指向不变的对象
#修正后的函数为
def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L
# 现在应该这样调用该函数
add_end(L = [1, 2, 3])
# 因为现在 l = none 是 默认参数

#------------------------------------------
# python 中，也支持可变参数
def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n*n
	return sum

#在定义可变参数的时候，多了一个 * 符号
#这样我们在调用函数的时候，可以不把参数自定义为 list 或者 tuple
calc(1, 2, 3, 4, 8)
#参数可以为任意个数
#当已经有一个 tuple 或者 list 的时候，想直接用该 list 或者 tuple, 可以在前面加一个 *

num = [1, 2, 3, 4]
calc(*num)
# * 号表示把这个 num 的所有元素作为可变参数传进去


#-----------------------------------------------------

# 关键字参数
# 关键字参数允许我们传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
	print('name', name, 'age', age, 'other', kw)

person('Adam', 35, gender = 'M', job = 'Engineer', city = 'Beijing')

# 用关键词参数，可以扩展函数的功能，是用户可以自定义一些可选参数

#也可以先自定义一个dict， 然后再把该dict转换成关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
#两种传参方式
#	1
person('Jack', 35, city = extra['city'], job = extra['job'])
#	2
person('Jack', 35, **extra)

# * 代表可变参数， ** 代表关键词参数
#	**extra 表示把extra这个dict的所有key-value用关键字参数传入到函数的 **kw 参数， kw将获得一个dict
#	kw获得的dict是extra的一个拷贝，对kw 的改动不会影响到额外的extra



#	命名关键词参数
#	以    person()	为例, 检查通过kw传入的参数
def person(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:', name, 'age:', job, kw)

#但是调用者依然可以传入不受限制的关键字参数

person('Jack', 24, city = 'Beijing', job = 'Engineer', addr = 'Zhuhai', zipcode = 3456789)

#如果要限制关键字参数的名字，就可以用命名的关键字参数
def person(name, age, *, city, job):
	print(name, age, city, job)

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
	print(name, age, args, city, job)
# 命名关键字必须传入参数名，否则就会报错
#命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city = 'Beijing', job):
	print(name, age, city, job)

person('Jack', 24, job = 'Doctor')
# 结果中的 city 将用默认值



#--------------------------------------------------------
#	参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

# 该函数参数包含 必选参数，必选参数，默认参数，可变参数，关键字参数
def f1(a, b, c = 0, *args, **kw):
	print(a, b, c, args, kw)

# 该函数参数包含 必选参数，必选参数，默认参数，命名关键字参数，关键字参数
def f2(a, b, c = 0, *, d, **kw):
	print(a, b, c, d, kw)









#--------------------------------------------------------
#	递归函数
# 在一个函数中调用它自己本身就叫做递归
# 以阶乘来举例
# fact(n) = n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n = fact(n-1) * n

def fact(x):
	if x == 1:
		return 1
	return n * fact(n-1)


# 在计算机中，函数调用是以栈（stack）来实现的，先进后出，调用函数就是加一层栈帧，返回就是减一层
# 从 n 一直进到 n == 1, 再从 n == 1 开始出（返回）
# 栈的大小是有限制的，因此要防止溢出


#	解决栈溢出的方式是‘尾递归’，尾递归和循环的逻辑差不多，可以把循环看成是一种尾递归
# 尾调要求在返回的时候只能出现自身调用，不能有其他形式的表达
def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num-1, num * product)

# 但其实 python解释器没有针对尾调进行优化，因此依然会出现溢出的问题，在这样的情况下使用loop更好


