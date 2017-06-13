#	现在来学习python的高级特性

#			切片

# 取一个 list 或者 tuple 的部分元素
 
 L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 现在要求取出 L 的前三个元素
# 1. 直接取
# 2. 用循环
	r = []
	for i in range(3):
		r.append(L[i])

# 3. 切片（slice）
	L[0:3]
# 从 0 开始，到 3 结束，包括 0，1，2
# 如果第一个索引是 0 ，还可以省略不写
	L[:3]

# 倒数切片
	L[-2:-1]
# 倒数切片默认最后一个值在 -1 位置
# -1 可省略不写


# 还可以规定切片的间隔
	L = list(range(100))
	L[0:50:5] == [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
	#表示取 0-49 的数，每间隔5个取一个

# 甚至可以用切片来复制 list
	L[:]
	# 可以返回其本身


# 还可以用来操作切片的有
	# tuple
	(0, 1, 2, 3, 4, 5)[:3]

	# str
	'ABCDEFG'[:3]
	'abcdefg'[::2] == 'aceg'



#-------------------------------------------------------------------------------

#		迭代

# 给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

#	dict
d = {'a': 1, 'b': 5, 'c': 6}
for key in d:
	print(key)
#默认情况下，dict 迭代的是key('a', 'b', 'c'),如果要迭代value, 用
	#	for value in d.items()
#同时迭代 key 和 value
	#	for k, v in d.items()


#	str
str = 'ABCDEEFG'
	for ch in str:
		print(ch)

# 如何判断一个对象是否可以迭代
#	通过 from collections import Iterable 语句
	   # isinstance(对象, Iterable)

from collections import Iterable
isinstance(str, Iterable)
# 返回结果为 bool

# 也可以将 list 转换为类似 java 的下标循环迭代
	#	enumerate() 函数
 for i, value in enumerate(['A', 'B', 'C']):
 	print(i, value)

 #上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
 for x, y in [(1, 1), (2, 2), (3, 3)]:
 	print(x, y)



#----------------------------------------------------------

#		列表生成式
list[1,2,3,4,5,6,7,8,9]
#	可以用
list(range(1,10)) # 来生成


#	先在要生成[1x1, 2x2, 3x3, ..., 10x10]
#	用循环
L = []
for x in range(1, 11):
	L.append(x * x)

#	用列表生成式
[x * x for x in range(1, 11)]
#把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
[x * x for x in range(1, 11) if x % 2 == 0]

#还可以使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ']
#结果为	['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
[d for d in os.listdir('.')]
# so.listdir('.') just a demo, not exists in this computer



# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 3, 'Y': 4, 'Z': 5}
for k, v in d.items():
	print(k, '=', v)
# 同样可以用列表生产式来完成
d = {'x': 3, 'Y': 4, 'Z': 5}
[k, '=', v for k, v in d.items()]

#把一个已有的list中所有的字符串变成小写：
L = ['HELLO', 'wORLD', 'nICE', 'tO', 'MEET', 'You']
[s.lower() for s in L]

#		练习，格式化一个含有数字跟字符的文本，将里面的大写全部变为小写
L = ['List', 'yeah', 'Fuck', 'This', 2017, 'world', 666]
[s.lower() for s in L if isinstance(s, str)]
#该方法错误，因为只保留了 str 到 s 当中

# 正确做法	1
[(i.lower() if isinstance(i, str) else i) for i in L]

#			2
def mylower(s):
    if isinstance(s, str):
        return s.lower()
    else:
        return s

L1 = ['Hello', 'World', 18, 'Apple', None]
L3 = [mylower(s) for s in L1]
print(L3)



#-------------------------------------------------------------------
#		生成器

#节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 方法1---把[] 换成 ()
g = (x * x for x in range(10))
# 通过 next() 函数获得下一个返回值
next(g)
next(g)
#...
# 当没有更多元素时，抛出 StopIteration 错误
#	用 next() 只适合打印单个元素
#	用循环来遍历
g = (x * x for x in range(10))
for n in g:
	print(n)


#	斐波拉契数列
#	斐波拉契数列无法用简单的列表生成式表达，可以用函数来写
def fibonacci(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

# 方法2---用yield
# 重新定义斐波拉契数列
def fibonacci(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

# 在调用时，通常不会用next()来逐个打印，一般用一个for循环
# 但是因为yield 的机制，在遇到 yirld 的时候就会停止，所以简单的调用不会看到
# done， 所以加一个抛出机制如下：
g = fib(10)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# 每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield (3)
	print('step 3')
	yield (5)


#		练习---杨辉三角
def yhsj(row):
	L = [1]
	for n in range(row):
		yield L
		L = [1] + ([x + y for x, y in zip(L[0 : -1], L [1 : 0])]) + [1]
		print(L)


# ---------------------------------------------------------------------------
#     迭代器
# 可以直接作用于 for 循环的数据类型有 list tuple dict set str
#								 以及 generator   带 yield 的 generator function

#		可作用于 for 循环的对象统称为可迭代对象： Iterable
# 检测一个对象是否可以迭代
from collections import Iterable
isinstance([], Iterable)

#	迭代器 ： Iterator
#	可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#	可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
isinstance((x for x in range(10)), Iterator)

#	生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

# 但是可以把 list/ dict/ str 等 Iterble 变成 Iterator， 使用 iter() 函数
isinstance(iter([]), Iterator) == True
isinstance(iter('abc'), Iterator) == True





