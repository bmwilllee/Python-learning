#			模块

#	像java 一样通过模块和包来组织整个程序
#	一个 .py 文件就是一个模块
#	包（Package）用来存放模块，不同包名下的模块可以有相同的模块名，因为他们的包名不同，所以可以用区分

#		注意：每一个包下面都得有一个 __init__.py 文件，这个文件用来规定这个目录是一个包
#			  __init__.py 可以是一个空文件，也可以有 Python 代码

#		与 java 一样，	python 可以有多级目录，组成多层次的包结构

#		在创建自己的模块是要注意，不能和Python中自带的模块名相同，否则将无法导入系统自带的模块



#------------------------------------------------------------------------------

#			使用模块

#	Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用
#	我们以内建的sys模块为例，编写一个hello的模块：


#！/user/bin/env python3
# -*- conding: utf-8 -*-

'a test module'

__author__ = 'WILLLEE'

import sys
def test():
 	args = sys.argv
 	if len(args) == 1:
 		print('Hello World !')
 	elif len(args) == 2:
 		print('Hello, %s' % args[1])
 	else:
 		print('Too many arguments !')

if __name__ == '__main__':
 	test()


#	第1行和第2行是标准注释 :
#		第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
#		第2行注释表示.py文件本身使用标准UTF-8编码

#	第4行是一个字符串 ： 
#		表示模块的文档注释
#		任何模块代码的第一个字符串都被视为模块的文档注释

#	第6行使用__author__变量把作者写进去

#	sys 的 argv 变量用 list 存储了命令行的所有参数，argv 至少由一个元素，因为第一个参数永远是该.py文件的文件名

#	当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
#	而如果在其他地方导入该hello模块时，if判断将失败
#	因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。


#----------------------------------------------------------------------

#		作用域
#	类似与 java 中的权限----private/public...

#	正常的函数名 ---- public
#	__xxx__	     ---- 特殊变量 (可以被直接引用，但有特殊用途，如 __author__ , __name__ 等)
#	__xxx 		 ---- private (不应该被直接引用)

# 看例子：
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

#	我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了
#	调用greeting()函数不用关心内部的private函数细节
#	这也是一种非常有用的代码封装和抽象的方法



#----------------------------------------------------------------------------

#		安装第三方模块

#	在Python中，安装第三方模块，是通过包管理工具pip完成的
#	Mac 或 Linux 无需安装 pip >_>
#	