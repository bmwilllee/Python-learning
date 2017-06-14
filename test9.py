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

	def __setattr__(seld, key, value):
		sel[key] = value



#	现在我们来编写一个针对上面代码的元测试：

import unittest

from mydict import Dict

class TestDict(unittest.TesrCase):
	"""docstring for TestDict"""
	def __init__(self):
		d = Dict(a = 1, b = 'test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
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

#		NOW, LET'S START OUR TEST !
