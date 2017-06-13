#		高阶函数  -- High-order Function

# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

# 在python 中， 变量名是可以指向一个函数的，因此函数名本身也就是一个变量名
# 在python中，内置函数其实也是通过包来引入的
# 比如 abs 函数其实是引入了 builtins 包，而 abs 只是该函数的默认变量名

def add(x, y, f):
	return f(x) + f(y)

# 调用该函数
add(-5, -10, abs)

# 编写高阶函数，就是让函数的参数能够接收别的函数。



# -------------------------------------------------------------------

#	map() 和 reduce() 函数

#		map()
#	map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 首先用生成器来做
L = [x * x for x in range(10)]

# 用map()
def f(x):
	return x * x

# 也可以这样
L = [f(x) for x in range(10)]

r = map(f, range(10))
list(r)
# r 得到的是 <map object at 地址>
#要调用list()来返回整个数列

# map() 在某些情况下很简洁：
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 返回
['1', '2', '3', '4', '5', '6', '7', '8', '9']


#		reduce()
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算:

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 求和
reduce(add, [1, 3, 5, 7, 9]) == 25
#当然，求和运算可以直接用python的sun()函数，reduce()主要针对其他的复杂运算

# 可以用 map() 结合 reduce() 来将 数字 str 转换成 int
from functools import reduce
def fn(x, y):
	return x * 10 + y

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

reduce(fn, map(char2num, '123456')) == 123456

#  整理成一个函数就是，这样就可以直接调用函数进行模糊转换，相当于自己做了一个int()函数
from functools import reduce
def strToInt(s):
	def fn(x, y):
		return x * 10 + y
	def charTonum(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(charTonum, s))

# 还可以用 lambda 函数进一步简化：
from functools import reduce
def charTonum(s):
	return:{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def strToint(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))


#		练习
#	1.将用户输入的名字格式化为首字母大写，其余小写
def formatName(name):
	return name[0].upper() + name[1:].lower()

def prod(s):
	return reduce(lambda x, y: x * y, s)



#		filter

# Python内建的filter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素


# 自动筛选出 列表 中的奇数
def is_odd(n):
	return n % 2 == 1
# return True / False
list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 把一个序列中的空字符删掉
def not_empty(s):
	return s and s.strip()

list(filter(not_empty, ['A', '', None, 'B', 'C']))
# 结果集为：['A', 'B', 'C']


# --------------------------------------------------------

#	埃氏筛法 筛选素数

# 首先，做一个生成器，来生成一个无限序列
def _odd_iter():
	n = 1
	while True:
		n = n + 1
		yield n

# 再定义一个筛选器
def _not_divisible(n):
	return lambda x: x % n > 0

# 最后定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it) #构造新序列

# 在调用的时候，需构造一个推出条件，否则这个函数将一直执行下去
for n in primes():
	if n < 1000:
		print(n)
	else:
		break



#-----------------------------------------------------------------
#		sorted
#	Python内置的sorted()函数就可以对list进行排序:
sorted([36, 12, 65, -34, 21, 0])

#	sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
sorted([36, 5, -12, 9, -21], key = abs)


#	字符串排序
# 默认情况下，字符串排序是按照ASCII的大小来比较的，大写在前，小写在后
# 如要忽略大小写，按照字母顺序排序：
sorted(['bob, About, Zoo, credit'], key = str.lower)
# 如果要进行反向排序：
sorted(['bob, About, Zoo, credit'], key = str.lower, reverse = True)

# -----------------------------------------------------------------
#		返回函数
#	高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def lazy_sum(*args):	# 参数为一个可变参数
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum    		# 注意，最后的返回值是 sum 这个函数名

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：

f = lazy_sum(1, 3, 5, 7, 9)
f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
#调用函数f时，才真正计算求和的结果：
f() == 25


# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1==f2
False

#	闭包
def count():
	fs = []
	for i in range[1, 4]:
		def f():
			return i * i
		fs.append(f)
	return fs
 f1, f2, f3 = count()

# 函数的结果为：
f1 == f2 == f3 == 9
# 原因就在于返回的函数引用了变量i，但它并非立刻执行
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# 如果一定要用到循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量的当前值
# 无论该循环变量后续如何更改，已经绑定导函数的变量不变

def count():
    def f(j):          # |
        def g():       # |___该部分属于 f(), 该函数传入参数 j，返回其内部子函数 g
            return j*j # |
        return g       # |
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
 # 再看看结果：
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9



#		匿名函数

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
 list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
 # 匿名函数其实就是：
 	def f(x):
 		return x * x

 #	关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数
 #	匿名函数有个限制，就是只能有一个表达式，不能写 return ，返回值就是该表达式的结果

 #	用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突
 #	此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
f(5) == 25

#	同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y


 #		装饰器


 #	函数对象有一个 _name_属性，可以拿到函数的名字：
 now.__name__  # 注意，是双下划线
 'now'

 #	现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志
 #	但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

#	本质上，decorator就是一个返回函数的高阶函数
#	所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
	def wrapper(*args, **kw):
		print('call %s(): ', % func.__name__)
		return func(*args, **kw)
	return wrapper
#	我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
	print('2015-3-25')




#		偏函数

#	Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
#	在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

#	以 int() 函数为例
#	int() 函数可以把字符串转换为整数，当仅传入字符串时，int() 函数默认按照十进制转换：
#	但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
int('12345', base=8)
int('12345', base=16)

#	假设要批处理二进制字符串，我们可以定义一个int2()，把默认值 base = 2传进去
def int2(x, base=2):
	return int(x, base)

#	注意，调用base是指输入字符串是base的值，默认值为10，而int的输出值一直都是base = 10



#	简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值）
#	返回一个新的函数，调用这个新函数会更简单。

#	functools.partial 可以帮助我们创建一个偏函数，不需要自己去定义：
import functools
int2 = functools.partial(int, base=2)
# 现在就可以调用 int() 来将二进制的字符串转换为十进制的数字
# 相比之前的 自定义 函数过程而言更简便

# 跟函数定义的方式一样，当我们想要操作其他进制时：
int2('1000000000', base=10)



int2 = functools.partial(int, base=2)
#实际上固定了int()函数的关键字参数base，也就是：
int2('10010')
#相当于：
kw = { 'base': 2 }
int('10010', **kw)



#当传入：

max2 = functools.partial(max, 10)		# 因为10是可变参数，因为不带变量名，所以属于 *aegs 而不是 **kw
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)
#相当于：
args = (10, 5, 6, 7)
max(*args)


