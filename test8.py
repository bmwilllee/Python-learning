#				错误调试和测试

#------------------------------------------------------

#	错误处理
#	1. 错误码方式处理
def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r == (-1):
		print('Error')
	else:
		pass

#		这样的错误方式处理方式十分不便，因为函数本身应该返回的
#		正常结果和错误码混在一起，造成调用者必须使用大量的代码来判断是否出错：

#		一旦出错，还要一级一级向上上报，知道某个函数可以处理错误（比如，用户给出的一个错误信息）
#		所以高级语言通常都内置了一套 try...e=xcept...finally... 的错误处理机制：

try:
	print('try...')
	r = 10 / 0
	print('result: ', r)
except ZeroDivisionError as e:
	print('except: ', e)
finally:
	print('finally...')
print('END')


#	跟 JAVA 不一样的是， PYTHON 的异常处理机制用的是 EXCEPT
#	而不是 JAVA 的 CATCH

#	在在上面的代码中，由于 0 无法作为除数，所以执行到算数着一行之后
#	程序会出错，然后跳转到 except 处理

#	finally 是肯定会被执行的部分


#		现在来看捕获 exception 的不同类型：
try:
	print('try...')
	r = 10 / int('a')
	print('result: ', r)
except ValueError as e:		# int() 函数可能会抛出 valueError
	print('ValueError: ', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError: ', e)
else:
	print('no error !')		# 如果没有发生错误，可以在 except 后面加一个 else
finally:
	print('finally...')
print('END')


#	跟 java 一样， python 的错误其实也是 class
#	并且所有的错误类都继承自 BaseException，所哟在使用 except 
#	时需要注意，它不但不捕获该类型的错误，还会把其他子类一网打尽

#	在下面这个例子中：
try:
	foo()
except ValueError as e:
	print('Valur...')
except UnicodeError as e:
	print('unicode...')

#	因为 UnicodeError 是 ValueError 的子类，所以即使存在
#	UnicodeError 错误，在 ValueError 就已经被干掉了，永远也轮不到它
#	因此我们在编程的时候要避免这些问题，至少要将子类错无先放到上面，父类错误放到下面

#	使用try...except捕获错误还有一个巨大的好处
#	就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

#	也就是说，不需要在每个可能出错的地方去捕获错误
#	只要在合适的层次去捕获错误就可以了。这样一来
#	就大大减少了写try...except...finally的麻烦

#-------------------------------------------

#		调用栈堆

#	如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获
#	打印一个错误信息，然后程序退出。来看看err.py：

# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')		# 错误源头

mian()


#	执行，结果如下：

$ python3 err.py
Traceback (most recent call last):
  File "err.py", line 11, in <module>
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero

#-------------------------------------------------

#		记录错误

#	如果不捕获错误，自然可以让Python解释器来打印出错误堆栈
#	但程序也被结束了。
#	既然我们能捕获错误，就可以把错误堆栈打印出来
#	然后分析错误原因，同时，让程序继续执行下去。

#Python内置的logging模块可以非常容易地记录错误信息：

import logging
def foo(s):
	return 10 / int(s)

def bar(s):
	return f00(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print('END')

#	同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
$ python3 err_logging.py
ERROR:root:division by zero
Traceback (most recent call last):
  File "err_logging.py", line 13, in main
    bar('0')
  File "err_logging.py", line 9, in bar
    return foo(s) * 2
  File "err_logging.py", line 6, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END

#-----------------------------------------------

#	抛出错误

#	因为错误是class，捕获一个错误就是捕获到该class的一个实例
#	因此，错误并不是凭空产生的，而是有意创建并抛出的
#	Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误


#		如果要抛出错误，首先根据需要，可以定义一个错误的class
#		选择好继承关系，然后，用raise语句抛出一个错误的实例：

class FooError(ValueError):
	"""docstring for FooError"""
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value : %s', % s)
	return 10 / n

foo('0')

#		执行，可以最后跟踪到我们自己定义的错误：

#		只有在必要的时候才定义我们自己的错误类型。
#		如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

#	最后，我们来看另一种错误处理的方式：
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise 			# raise 的意思是将这个错误继续向上一级抛出
        				# 上抛的原因是因为当前所处的代码块解决不了当前的错误类型

bar()

#	raise语句如果不带参数，就会把当前错误原样抛出
#	此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')

#	只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。


#------------------------------------------------------------------


#			调试
#	此章来讲 BUG 的修复
#	在检验 bug 的时候，使用 print() 直接将可能出错的地方打印出来是最常见的办法
#	但是这样做未来还得把 print() 的地方删掉，就显得很麻烦

#	方法 1  ---  断言
#	凡是用 print() 来排错的地方，都可以用 '断言' （assert）：

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'	# 表达式n != 0应该是True
    							# 否则，根据程序运行的逻辑，后面的代码肯定会出错
    							# 如果断言失败，assert语句本身就会抛出AssertionError
    							# 并且会打印出 'n is zero'
    return 10 / n

def main():
    foo('0')


#	在启动 Python 解释器的时候，可以用 -0 参数来关闭代码中所有的 assert
#	关闭 assert 之后，你可以把 assert 都看成是 pass

#----------------------

#	方法 2	---   logging

#	把 print() 换成 logging 是第二种方式
#	和assert比，logging不会抛出错误，而且可以输出到文件：

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#	logging的好处，它允许你指定记录信息的级别
#	有debug，info，warning，error等几个级别
#	当我们指定level=INFO时，logging.debug就不起作用了
#	同理，指定level=WARNING后，debug和info就不起作用了
#	这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息

#	logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件

#-----------------------

# 方法 3  ---   pdb

#	启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# err.py
s = '0'
n = int(s)
print(10 / n)

#	pdb 的主要操作：
#					1. python3 -m pdb err.py(文件名) --- 以参数 -m pdb 启动
#					2. 1 --- 查看代码
#					3. n --- 单步执行代码
#					4. p 变量名 --- 查看变量
#					5. q --- 结束调试，退出程序


#	这种通过pdb在命令行调试的方法理论上是万能的
#	但实在是太麻烦了，如果有一千行代码
#	要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法：

#----------------------------

# 方法 4  ---  pdb.set_trace()

#	这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb
#	然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：

# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

#	运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境
#	可以用命令p查看变量，或者用命令c继续运行：
$ python3 err.py 
> /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
-> print(10 / n)
(Pdb) p n
0
(Pdb) c
Traceback (most recent call last):
  File "err.py", line 7, in <module>
    print(10 / n)
ZeroDivisionError: division by zero


#	这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。
#	最好的方式当然是使用 IDE 啦