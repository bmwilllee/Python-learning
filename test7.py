#				面向对象高级编程

#----------------------------------------------------------------

# 使用 __slots__

#	对于动态语言，当我们创建了一个对象的实例之后，我们可以给该实例绑定任何属性和方法

class Student(object):
	"""docstring for Student"""
	pass

s = Student()
s.name = 'Will'						#首先给该实例绑定一个属性

def set_age(self, age):				#定义一个方法
	self.__age = age

from type import MethodType
s.set_age = MethodType(set_age, s)	#给实例绑定这个方法
s.set_age(20)						#调用实例方法
s.age 								#测试结果

#	但是，对实例绑定 方法 ，对另外一个实例是不起总用的

#	但是可以在 class 外给 class 绑定方法，这样所有的实例都拥有这个方法

def set_score(self, score):
	self.__score = score

Student.set_score = set_score		#给 class 绑定方法

#		绑定方法之后所有的 class 都可以调用这个方法


#	__slots__
#	为了限制实例的属性，Python 允许在定义 class 的时候，定义一个特殊的 __slots__
#	来限制该 class 实例能添加的属性：

class Student(object):
	"""docstring for Student"""
	__slots__ = ('name', 'age')		# 用tuple定义允许绑定的属性名称

# 在绑定属性的时候，如果所要绑定的属性不在这个范围内，则无法绑定
# 并且你将得到 AttributeError 的错误



#--------------------------------------------------------------------------------

#	使用 @property

# 在绑定属性的时候，我们应该限制某些属性的范围
class Student(object):

	__slots__ = ('name', 'age')

    def get_score(self):
         return self._score

    def set_score(self, value):	#通过一个set_score()方法来设置成绩，这样可以检查传入的参数
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# 但是，上面的方法又略显复杂，不符合 Python 的哲学

#	我们可以用 @property 装饰器来解决调用的上的复杂

class Student(object):

	__slots__ = ('name', 'age')

    @property		# 把一个getter方法变成属性，只需要加上@property就可以了
    def score(self):
        return self._score

    @score.setter	# @property本身又创建了另一个装饰器@score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# score.setter 负责把一个 setter 方法变成属性赋值，于是我么就有了一个可控的属性操作

s1 = Student()
s1.score = 60	# OK，实际转化为s.set_score(60)
s1.score 		# # OK，实际转化为s.get_score()

 s.score = 9999 # 不行，因为超出了属性规定的范围


#		还可以之定义只读属性，之定义 getter 方法，不定义 setter 方法就是一个只读属性

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property  # age 是一个只读属性，可以用来自动计算用户的年龄
    def age(self):
        return 2015 - self._birth

		

# 小结

#	@property广泛应用在类的定义中，可以让调用者写出简短的代码
#	同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性


#-------------------------------------------------------------------------------

#	多重继承


class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

#	接下来定义具体的小类

class Dog(Mammal， Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass


#		Mixln （Mix Inherance）

#	让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn
#	MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候
#	我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系

#	Python 自带了 TCPServer 和 UDPServer 这两类网络服务，通过这些服务的多继承
#	我们可以创造出合适的服务来

#		编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

#		编写一个多线程模式的UDP服务，定义如下：
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

#	如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass




#--------------------------------------------------------------------------------

# 定制类

#	Python 中有许多类似 __xxx__ 这样的特殊用途的函数，可以帮助我们定制类

__str__

class Student(object):
	def __init__(self, name):
        self.name = name

	print(Student('Michael'))
#		返回：
#		<__main__.Student object at 0x109afb190>

#	为了避免打印出这些用户看不懂的信息，需要借助 __str__

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name

s2 = Student('Mike')
# 如果直接在控制台上调用 s，而不用 print()
# 会打印出 <__main__.Student object at 0x109afb310>

#	因为直接调用 s 调用的是 __repr__ 而不是 __str__
#	我们可以重新定义一下这个 class


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__


#------------------------------------

__iter__

#	如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
#	该方法返回一个迭代对象，然后，Python的for循环就会不断调用该
#	迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0, 1	# 初始化两个计数器a，b

	def __iter__(self):
		return self				# 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值
		if self.a > 100000:		# 退出循环的条件
			raise StopIteration()
		return self.a 			# 返回下一个值

#	现在，来调用 Fib 实例作用于 for 循环

>>> for n in Fib():
...     print(n)
...
1
1
2
3
5
...
46368
75025

#-----------------------------------

__getitem__

# Fib实例虽然能作用于for循环，看起来和list有点像
# 但是，把它当成list来使用还是不行，比如，取第5个元素：
>>> Fib()[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fib' object does not support indexing

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法:
 class Fib(object):
 	"""docstring for Fib"""
 	def __getitem__(self, n):
 		a, b = 1, 1
 		for x in range(n):
 			a, b = b, a + b
 		return a

#	现在，就可以按下标访问数列的任意一项了：

>>> f = Fib()
>>> f[0]
1
>>> f[1]
1
>>> f[2]
2
>>> f[3]
3
>>> f[10]
89
>>> f[100]
573147844013817084101

# 但是list有个神奇的切片方法：
>>> list(range(100))[5:10]
[5, 6, 7, 8, 9]

# 对于Fib却报错
# 原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
# 所以要做判断：

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):   # 以stop作为结束条件
                if x >= start:		# 从 x = start 开始 sppend 到 L 中
                    L.append(a)
                a, b = b, a + b
            return L

# 现在试试Fib的切片：
>>> f = Fib()
>>> f[0:5]
[1, 1, 2, 3, 5]
>>> f[:10]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# 但是没有对step参数作处理：
>>> f[:10:2]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]



# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的


#-----------------------------------------

__getattr__

# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：

class Student(object):
    def __init__(self):
        self.name = 'Michael'

# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
>>> s = Student()
>>> print(s.name)
Michael
>>> print(s.score)
Traceback (most recent call last):
  ...
AttributeError: 'Student' object has no attribute 'score'


# 要避免这个错误，除了可以加上一个score属性外
# Python还有另一个机制，那就是写一个__getattr__()方法
# 动态返回一个属性。修改如下：

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')
# 来尝试获得属性，这样，我们就有机会返回score的值：

>>> s = Student()
>>> s.name
'Michael'
>>> s.score
99

# 返回函数也是完全可以的：
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

# 只是调用方式要变为：
>>> s.age()
25

# 此外，注意到任意调用如s.abc都会返回None
# 这是因为我们定义的__getattr__默认返回就是None
# 要让class只响应特定的几个属性
# 我们就要按照约定，抛出AttributeError的错误：

class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


#	利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

#	试试：
>>> Chain().status.user.timeline.list
'/status/user/timeline/list'



#-----------------------------------

__call__

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

# 调用方式如下：

>>> s = Student('Michael')
>>> s() 						# self参数不要传入
My name is Michael.


#	Python 允许我们将对象看成是一个函数
#		如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来
#		因为类的实例都是运行期创建出来的
#		这么一来，我们就模糊了对象和函数的界限

# 那么，怎么判断一个变量是对象还是函数呢？
#	更多的时候，我们需要判断一个对象是否能被调用
#	能被调用的对象就是一个Callable对象
#	比如函数和我们上面定义的带有__call__()的类实例：

>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False



#----------------------------------------------------------------------------

#			使用枚举类

#	当我们需要定义常量时，一个办法是通过大写变量通过整数来定义，例如月份：
JAN = 1
FEB = 2
MAE = 3
#	好处是简单，确定是 int 类型，任然属于变量

#	更好的办法是为这样的枚举类型定义一个 class 类型，每个常量都是 class 的唯一一个实例
#	 Python 提供了 Enum 类来实现这个功能

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#	这样我们就获得了 Month 的枚举类型，可以直接使用 Month.Jan 来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

#	输出结果为：
Jan => Month.Jan, 1
Feb => Month.Feb, 2
...

#		value 属性是自动赋给成员的 int 常量， 默认从 1 开始

#	如果要更精确的控制枚举类型，可以从 Enum 派生出自定义类：

from enum import Enum, unique

@unique	#	unique 装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
	"""docstring for Weekday"""
	Sun = 0 # Sun 的 value 被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6


#	访问这些枚举类型可以由若干的办法：
>>> day1 = Weekday.Mon
>>> print(day1)
Weekday.Mon
>>> print(Weekday.Tue)
Weekday.Tue
>>> print(Weekday['Tue'])
Weekday.Tue
>>> print(Weekday.Tue.value)
2
>>> print(day1 == Weekday.Mon)
True
>>> print(day1 == Weekday.Tue)
False
>>> print(Weekday(1))
Weekday.Mon
>>> print(day1 == Weekday(1))
True
>>> Weekday(7)
Traceback (most recent call last):
  ...
ValueError: 7 is not a valid Weekday
>>> for name, member in Weekday.__members__.items():
...     print(name, '=>', member)
...
Sun => Weekday.Sun
Mon => Weekday.Mon
Tue => Weekday.Tue
Wed => Weekday.Wed
Thu => Weekday.Thu
Fri => Weekday.Fri
Sat => Weekday.Sat


# 枚举的继续学习

#枚举，相当于自己当以了一种数据类型  like int，str

#	1.首先，定义枚举要导入enum模块。
#	2.枚举定义用class关键字，继承Enum类。
#	3.用于定义枚举的class和定义类的class是有区别

from enum import Enum

class Color(Enum):
	"""docstring for Color"""
	red = 1
	orange = 2
	yellow = 3
	blue = 4
	green = 5
	black = 6
	white = 7

#	定义枚举时，成员名称不允许重复
#	默认情况下，不同的成员值允许相同
#	但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名

red = 1
red_alias = 1

#	成员Color.red和Color.red_alias具有相同的值
#	么成员Color.red_alias的名称red_alias就被视作成员Color.red名称red的别名

#	如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
print(Color(1))
#	输出结果为 Color.red

#	如果要限制定义枚举时，不能定义相同值的成员
#	可以使用装饰器@unique【要导入unique模块】

from enum import Enum, unique

@unique
class Color(Enum):
	"""docstring for Color"""
	red = 1
	red_alias = 1


#	因为已经规定了unique, 那么这样定义相同的值就会报错



#	2 枚举取值

#		2.1 通过成员的名称来获取成员
Color['red']

#		2.2 通过成员值来获取成员
Color(2)

#		2.3 通过成员，来获取它的名称和值
red_member = Color.red



#	3 迭代器
#		3.1 枚举支持迭代器，可以遍历枚举成员

for color in Color:
	print(color)

#	3.2 如果枚举有值重复的成员，循环遍历枚举时只获取值重复成员的第一个成员

#	3.3 如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__

for color in Color.__members__.items



#	4. 枚举比较

#		4.1 枚举成员可进行同一性比较
Color.red is Color.red == True
Color.red is not Color.blue == True

#		4.2 枚举成员可进等值比较
Color.blue == Color.red

#		4.3 枚举成员不能进行大小比较
Color.red < Color.blue





#----------------------------------------------------------------------------

#			使用元类

#		什么是元类，元类就是我们创建的类

#	type()

#	动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
#	我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数

#	type()函数既可以返回一个对象的类型，又可以创建出新的类型
#	我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

# 现在我们 直接采用运行语句的方式来动态创建一个 Hello 类，用 type() 函数
def fn(self, name = 'world'):		# 先定义一个这个类中要用到的 函数
	print('Hello, %s.' %name)


# 现在来动态创建我们的类
Hello = type('Hello', (object,), dict(hello = fn))	# 创建 hello class

# (object,) 其实是 tuple 的单元素写法，因为 Python 是支持多继承的

# 要创建一个class对象，type()函数依次传入3个参数：
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

#	通过type()函数创建的类和直接写class是完全一样的
#	因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法
#	然后调用type()函数创建出class

#			Python 编译器在创建类的时候，其实就是调用了 type() 函数！！！！！！！



#	-------------------------------------

#		metaclass

#	除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
#	metaclass，直译为元类

#	当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
#	但是如果我们想创建出类呢？
#	那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
#	连接起来就是：先定义metaclass，就可以创建类，最后创建实例

#	metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
#	metaclass是Python面向对象里最难理解，也是最难使用的魔术代码


#		定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾：
class ListMetaclass(type):
	"""docstring for ListMetaclass"""
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

#		有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass = ListMetaclass):
	"""docstring for MyList"""
	pass

#		当我们传入关键字参数metaclass时，魔术就生效了
#		它指示Python解释器在创建MyList时
#		要通过ListMetaclass.__new__()来创建

#		在此，我们可以修改类的定义，比如:
#		加上新的方法，然后，返回修改后的定义

#	__new__()方法接收到的参数依次是：
#	当前准备创建的类的对象；
#	类的名字；
#	类继承的父类集合；
#	类的方法集合.

# 测试一下MyList是否可以调用add()方法：

>>> L = MyList()
>>> L.add(1)
>> L
[1]

# 而普通的list没有add()方法：

>>> L2 = list()
>>> L2.add(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'

#	动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？
#	正常情况下，确实应该直接写，通过metaclass修改纯属变态。
#	但是，总会遇到需要通过metaclass修改类定义的。
#	ORM就是一个典型的例子。
#	ORM全称“Object Relational Mapping”，即对象-关系映射
#	就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表
#	这样，写代码更简单，不用直接操作SQL语句。

#	要编写一个ORM框架，所有的类都只能动态定义
#	因为只有使用者才能根据表的结构定义出对应的类来


#	让我们来尝试编写一个ORM框架：
#		编写底层模块的第一步，就是先把调用接口写出来
#		比如，使用者如果使用这个ORM框架
#		想定义一个User类来操作对应的数据库表User
#		我们期待他写出这样的代码：

class User(Model):
	"""docstring for User"""
	# 定义类的属性到列的映射：
	id = integerField('id')
	name = StringField('name')
	email = StringField('email')
	password = StringField('password')

# 创建一个实例：
u = User(id = 123456, name = 'Will', email = '986852442@qq.com', '123456789')
#保存到数据库：
u.save()

#	其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的
#	剩下的魔术方法比如save()全部由metaclass自动完成
#	虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单

# 现在，我们就按上面的接口来实现该ORM
#	首先来定义Field类，它负责保存数据库表的字段名和字段类型：

class Field(object):
	"""docstring for Field"""
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s: %s>' % (self.__class__.__name__, self.name)

#	在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：

class StringField(Field):
	"""docstring for StringField"""
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	"""docstring for IntegerField"""
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')
		
#	下一步，就是编写最复杂的ModelMetaclass了：

class ModelMetaclass(type):
	"""docstring for ModelMetaclass"""
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s' % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mappings: %s ==> %s' % (k, v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = name # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)

#	以及基类Model：
class Model(dict, metaclass = ModelMetaclass):
	"""docstring for Model"""
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v, name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s(%s) values ($s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))

