#			IO编程

#	几个重要的概念：
#					1. I/O
#					2. Stream
#					3. 同步IO
#					3. 异步IO

#	异步IO 编写的程序性能远远高于同步IO，但是异步IO的缺点是编程模型复杂
#	因为异步IO需要有“通知” ———— 回调/轮询

#	操作IO的能力都是由操作系统提供的
#	每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用
#	ython也不例外。我们后面会详细讨论Python的IO编程接口



#	为了便于学习，这一章关于IO的学习我们都采用同步IO,后续涉及到服务器端程序开发时我们再讨论异步IO


#------------------------------------------------------------------------------------------------------

#			文件读写

#	读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的
#	读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的
#	现代操作系统不允许普通的程序直接操作磁盘
#	所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符）
#	然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）

#		读文件

# 	要以读文件的模式打开一个文件对象
#	使用Python内置的open()函数，传入文件名和标示符：

f = open('/Users/weigirl/learngit/readme.txt', 'r')
#	'r' 表示只读，这个跟 C 是一样的

#	如果文件不存在，open()函数就会抛出一个IOError的错误
#	且给出错误码和详细的信息告诉你文件不存在

'''
>>> f=open('/Users/weigirl/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Users/weigirl/notfound.txt'

'''

#	如果文件打开成功，调用 f.read() 可以一次性读取全部内容
#	Python把内容读到内存，用一个str对象表示：

#	最后一步是调用close()方法关闭文件
#	文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
#	并且操作系统同一时间能打开的文件数量也是有限的：
f.close()

#	由于文件读写时都有可能产生IOError, 一旦出错，后面的f.close()就不会调用
#	所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

try:
	f = open('/Users/weigirl/learngit/readme.txt', 'r')
	f.read()
finally:
	if f:
		f.close()

#		但是每次都这么写实在太繁琐
#		所以，Python引入了with语句来自动帮我们调用close()方法：
with open('/Users/weigirl/learngit/readme.txt', 'r') as f:
	print(f.read())
#		这和前面的try ... finally是一样的，但是代码更佳简洁
#		并且不必调用f.close()方法



#	调用read()会一次性读取文件的全部内容，如果文件有10G，内存就会爆炸
#	所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容
#	另外，调用readline()可以每次读取一行内容
#	调用readlines()一次读取所有内容并按行返回list
#	因此，要根据需要决定怎么调用

#	如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险
#	如果是配置文件，调用readlines()最方便：

	for line in f.readlines():
		print(line.strip())	 # 把末尾的'\n'删掉

#	这样就可以逐行打印出文本的内容


#		二进制文件
#	前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件
#	要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('Users/weigirl/Pictures/pictures/Desert.jpg', 'rb')
f.read()

#	输出结果为：
'''
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...'  #十六进制表示的字节
'''



#		字符编码
#	要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
#	例如，读取GBK编码的文件：

f = open('/Users/weigirl/gbk.txt', 'r', encoding='gbk')
f.read()

#	遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError
#	因为在文本文件中可能夹杂了一些非法编码的字符
#	遇到这种情况，open()函数还接收一个errors参数
#	表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('/Users/weigirl/gbk.txt', 'r', encoding = 'gbk', errors = 'ignore')



#		写文件
#	写文件和读文件是一样的，唯一区别是调用open()函数时
#	传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

 f = open('/Users/weigirl/learngit/readme.txt', 'w')
 f.write('Hello, git')
 f.close()

#	你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件
#	当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入
#	只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘
#	忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了
#	所以，还是用with语句来得保险：

with open('/Users/weigirl/learngit/readme.txt', 'w') as f:
	f.write('Hello, git')



#----------------------------------------------------------------------------


#			StringIO 和 BytesIO

#		StringIO
#	很多时候，数据读写不一定是文件，也可以在内存中读写
#	StringIO顾名思义就是在内存中读写str
#	要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
f.write('hello')
#	返回 5（此次写入的字符串长度）
f.write(' ')
#	同理，返回 1
f.write('world')
print(f.getvalue())
#	返回 hello world

#	getvalue() 方法用于获得写入的str

#	要读取 StringIO，可以用一个str初始化StringIO，然后，像读取文件一样读取：
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s = '':
		break
	print(s.strip())



#		BytesIO

#	StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
#	BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
#	返回 6 (在utf-8中，绝大多数中文占 3 个 byte)
print(f.getvalue())
#	返回	b'\xe4\xb8\xad\xe6\x96\x87'

#	请注意，写入的不是str，而是经过UTF-8编码的bytes
#	和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
#	返回	b'\xe4\xb8\xad\xe6\x96\x87'


'''
小结

StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
'''
