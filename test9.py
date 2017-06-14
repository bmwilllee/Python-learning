#			单元测试

#------------------------------------------------------------------

#	单元测试就是对一个模块或者一个函数进行正确性的检测

#比如对函数abs()，我们可以编写出以下几个测试用例：
#输入正数，比如1、1.2、0.99，期待返回值与输入相同；
#输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
#输入0，期待返回0；
#输入非数值类型，比如None、[]、{}，期待抛出TypeError

#	如果单元测试通过，说明我们测试的这个函数能够正常工作
#	如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过

#	单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改
#	只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影响

#	如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试


#	我们现在编写一个 Dict 来测试一下单元测试：
class Dict(object):
	"""docstring for ClassName"""
	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError as e:
			print('key Error.....')
			raise AttributeError(r"'Dict object has no attributes '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value



#	现在我们来编写一个针对上面代码的元测试：

import unittest			# 引入 Python 种自带的 unittest 模块

from mydict import Dict

class TestDict(unittest.TestCase):
	"""docstring for TestDict"""
	def __init__(self):
		d = Dict(a = 1, b = 'test')
		self.assertEqual(d.a, 1)	# 断言判断
		self.assertEqual(d.b, 'test')	# 断言判断
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyError(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	
	def test_attrError(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
#	编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
#	以test开头的方法就是测试方法
#	以test开头的方法不被认为是测试方法，测试的时候不会被执行

#	对每一个测试都要写一个 text_xxx() 方法，由于 unittest.TestCase 提供了很多内置的
#	条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的


#	最常见的断言就是 assertEqual():
self.assertEqual(abs(-1), 1)# 断言函数返回的结果与1相等
#	另一种重要的断言就是期待抛出制定类型的 Error , 比如通过d['empty']
#	访问不存在的 key 时，断言会抛出 KeyError：
with self.assertRaises(KeyError):
	value = d['empty']
#	而通过 d.empty 访问不存在的 key 时， 我们期待抛出 AttributeError:
with self.assertRaises(AttributeError):
	value = d.empty

#		NOW, LET'S START OUR TEST !

#--------------------------------

#		运行单元测试

#	最简单的方式是在 mydict_test.py 的最后加上两行代码：
if __name__ = '__name__':
	unittest.main()

#	这样就可以可以把测试文件 mydict_test.py 当作正常的 python 脚本运行：

$ python3 mydict_test.py

#	另一种方法是在命令行通过参数-m unittest直接运行单元测试：

$ python3 -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK


#	第二种是推荐的做法，因为这样一次可以批量运行很多单元测试
#	并且由很多工具可以自动来运行这些单元测试

#	-----------------------------

#	setUp 与 tearDown

#	可以在单元测试中编写两个特殊的setUp()和tearDown()方法
#	这两个方法会分别在每调用一个测试方法的前后分别被执行。

#	setUp()和tearDown()方法有什么用呢？
#	设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库
#	在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

class TestDict(unittest.TestCase):

#	这两个方法会在每次其他测试方法被调用时被自动执行
    def setUp(self):  #	调用于方法执行前
        print('setUp...') 

    def tearDown(self):	# 调用于方法执行后
        print('tearDown...')




#-----------------------------------------------------------------

#		文档测试

#	如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码
#	比如re模块就带了很多示例代码：
 import re
 m = re.search('(? <= abc)def', 'abcdef')
 m.group()

 #	当我们编写注释时，如果写上这样的注释：

 def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

#	无疑更明确地告诉函数的调用者该函数的期望输入和输出。
#	并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试

#	doctest 严格地按照 Python 交互式命令行的输入和输出来判断测试结果是否正确
#	只有测试异常的时候，可以用 ... 表示中间一大段烦人的输出

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

#	注意到最后3行代码:
#	当模块正常导入时，doctest不会被执行。只有在命令行直接运行时
#	才执行doctest。所以，不必担心doctest会在非测试环境下执行
