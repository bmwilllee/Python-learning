#			面向对象编程



#	跟java一样，首先定义一个学生类
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s\'s score is %s' % (self.name, self.score))


#	创建两个学生对象，然后调用他们的方法
BART = Student('Bart Simpson', 59)
Lisa = Student('Lisa', 87)
BART.print_score
Lisa.print_score


#------------------------------------------------------------

#			类和实例

#	和普通的函数相比，在类中定义的函数只有一点不同：
#	第一个参数永远是实例变量 self
#	并且，调用时，不用传递该参数
#	除此之外，类的方法和普通函数没有什么区别
#	所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

#	数据封装
#	封装就是在类中定义这个类应该有的参数，然后在类中定义调用这些参数的方法
#	并直接通过对象来调用

#---------------

#	和静态语言不同，Python允许对实例变量绑定任何数据
#	也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

BART.age = 8   #可以给BART新增一个 age 参数
#	并直接调用这个参数 ：
BART.age

# 单数对于 Lisa， 我们没有给她这个参数，如果调用的话程序就会报错：
Lisa.age



#-------------------------------------------------------------------


#			访问限制

__arg # private

#	我们把之前的 Student 的两个变量改为 private 来限制访问

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

#	这样使用者就无法从外部来修改这两个变量

#	如果要从外部访问对象的参数，可以在类中加入 get 方法
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def get_Score(self):
		return self.__name

	def get_Name(self):
		return self.__name

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))


#	如果允许外部修改score，可以在类中定义 set 方法
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def get_Score(self):
		return self.__name

	def get_Name(self):
		return self.__name

	def setName(self, name):
		this.__name = name

	def setScore(self, score):  # 通过这个方法，不仅满足从外部修改参数，还可以对参数做检查，避免非法变量的传入
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

#	有些时候，你会看到以一个下划线开头的实例变量名，比如_name
#	这样的实例变量外部是可以访问的，但是，按照约定俗成的规定
#	当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。


#		注意！
__xxx #  其实也是可以通过外部来访问的，但是因为 Python 把这个变量自动改成了 _Student__name
	  #	 所以，还是可以通过 _类名__变量名 的形式来访问的，但是，一切靠自觉 >_>




# --------------------------------------------------------------------------------

#			继承和多态

# 继承

#	首先，我们来定义一个 Animal 类
class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	"""docstring for Dog"""
	def eat(self):
		print('Dog is eating...')

	def run(self):
		print('Dog is running...')

class Cat(Animal):
	"""docstring for Cat"""
	def sleep(self):
		print('Cat is sleeping...')

	def run(self):
		print('Cat is running...')



#		在 oop 上， python 跟 java 都是差不多，也都由方法的覆盖，继承，多态的实现
#		在此就不做过多的叙述

#		多态的几种主要实现方式：
#		1. 继承
#		2. 覆盖
#		3. 重载
#		4. 前缀与后缀

#	我们在定义一个 class 的时候，其实就是定义了一种新的数据类型
#	学会用 isinstance() 来判断数据类型
a = Animal()
isinstance(a, Animal) == True

#	如果一个实例的数据类型是某个子类，那么它的数据类型同样属于它的父类
#	但是倒过来就不行

def run_twice(animal):
		animal.run()
		animal.run()


#		静态语言 VS 动态语言

#	对于静态语言（例如Java),如果需要传入 Animal 类型，传入对象必须是 Animal 类型或者它的子类
#	否则无法调用 run() 方法

#	而对于动态语言（例如Python），不一定是它的子类，只要保证传入对象有一个 run() 方法即可

class Timer(object):
	"""docstring for Timer"""
	def run(self):
		print('Start...')



#	----------------------------------------------------------------

#			获取对象信息

#	使用 type() 函数：

type(123)

#		如果一个变量指向函数或者类，也可以用type()函数
#		现在我们来看 type() 函数的放回类型
type(123) == type(456) == True
type(123) == int == True
type('123') == type('abc') == str == True

#		要判断一个对象是否是函数，可以使用types模块中定义的常量：
import types
def fn():
	pass

>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True


#	使用 isinstance() 函数

#	对于class的继承关系来说，使用type()就很不方便
#	我们要判断class的类型，可以使用isinstance()函数

#		isinstance()可以告诉我们，一个对象是否是某种类型。
#		先创建3种类型的对象：
a = Animal()
d = Dog()

isinstance(d, Dog)
isinstance(d, Animal)

#	能用 type() 判断的基本类型也能用 isinstance() 来判断
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)

#	并且还可以判断一个变量是否是某些类型中的一种：
isinstance([1, 2, 3], (list, tuple)) == True
isinstance((1, 2, 3), (list, tuple)) == True



#	使用 dir()
#		如果要获得一个对象的所有属性，可以使用 dir()

>>> dir('ABC')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#		所以，我们在调用 len() 方法时，实际上，在 len() 内部
#		它自动去调用该对象的 __len__() 方法，所以，下面的代码是等价的：

len('ABC') == 'ABC'.__len__()

#		我们自己写的类，如果也想直接让对象调用 len() 方法的话，就自己定义一个 __len__()方法：
class MyDog(object):
	"""docstring for MyDog"""
	def __len__():
		return 100

dog = MyDog()
len(dog)


#	配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x


obj = MyObject()

#		紧接着，可以测试该对象的属性：
hasattr(obj, 'x')	# 有属性'x'吗？
obj.x

hasattr(obj, 'y')	# 有属性'y'吗？

setattr(obj, 'y')	# 设置一个属性'y'
hasattr(obj, 'y')	# 有属性'y'吗？  True

getattr(obj, 'y')	# 获取属性'y'
obj.y 				# 获取属性'y'


#	如果试图获取不存在的属性，会抛出AttributeError的错误:
getattr(obj, 'z') 	# 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'


#	可以传入一个default参数，如果属性不存在，就返回默认值：

getattr(obj, 'z', 404) 	# 获取属性'z'，如果不存在，返回默认值404

#	也可以获得对象的方法：
hasattr(obj, 'power') 	# 有属性'power'吗？


		
#---------------------------------------------------------------------------

#			实例属性和类属性

# 由于Python是动态语言，根据类创建的实例可以任意绑定属性
#	给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

s1 = Student('Bob')
s1.score = 90

#	实例中的属性分为类属性和实例属性

#	实例属性的优先级高于类属性的优先级

class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student

