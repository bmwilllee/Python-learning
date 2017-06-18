#				ThthreadLocal

#-------------------------------------------------------------

#	在多线程环境下，每个线程都有自己的数据
#	一个线程使用自己的局部变量比使用全局变量好
#	因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁

#	但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
def process_student(name):
	std = Student(name)
	#	std 是局部变量，但是每个函数都要用它，因此必须传递进去：
	do_task_1(std)
	do_task_2(std)

def so_task_1(std):
	do_subtask_1(std)

def do_task_2(std):
	do_subtask_2(std)

#	每个函数一层一层调用都这么传参数那还得了？用全局变量？
#	也不行，因为每个线程处理不同的Student对象，不能共享

#	如果用一个全局dict存放所有的Student对象
#	然后以thread自身作为key获得线程对应的Student对象如何？

global_dict = {}

def std_thread(name):
	std = Student(name)
	#	把 std 放到全局变量 global_dict中：
	global_dict[threading.current_thread()] = std
	do_task_1()
	do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    ...

#	这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题
#	但是，每个函数获取std的代码有点丑
#	有没有更简单的方式?
#	ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
	#	获取当前线程关联的student
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	#	绑定ThreadLocal的student：
	local_school.student = name
	process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

#	执行结果：
Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)

#	全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响
#	你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量
#	可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理

#	可以理解为全局变量local_school是一个dict，不但可以用local_school.student
#	还可以绑定其他变量，如local_school.teacher等等

#	ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接
#	HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源


#小结

#	一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本
#	互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题



#	---------------------------------------------------------------------------------

#				进程 VS 线程

#------------------------------------------------------

#	我们介绍了多进程和多线程，这是实现多任务最常用的两种方式
#	现在，我们来讨论一下这两种方式的优缺点：

#	首先，要实现多任务，通常我们会设计Master-Worker模式
#		Master负责分配任务
#		Worker负责执行任务
#	因此，多任务环境下，通常是一个Master，多个Worker

#	如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker
#	如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker

#	多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程
#	当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低
#		著名的Apache最早就是采用多进程模式

#	多进程模式的缺点是创建进程的代价大
#	在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大
#	另外，操作系统能同时运行的进程数也是有限的
#	在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题

#	多线程模式通常比多进程快一点，但是也快不到哪去
#	而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃
#	因为所有线程共享进程的内存
#	在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：
#		“该程序执行了非法操作，即将关闭”
#	其实往往是某个线程出了问题，但是操作系统会强制结束整个进程

#	在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式
#	由于多线程存在稳定性的问题，IIS的稳定性就不如Apache
#	为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂


#			线程切换

#	操作系统在切换进程或者线程时
#	它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等）
#	然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才开始执行
#	这个切换过程虽然很快，但是也需要耗费时间
#	如果有几千个任务同时进行，操作系统可能就主要忙着切换任务
#	根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态

#	以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好



#			计算密集型 vs. IO密集型

#	是否采用多任务的第二个考虑是任务的类型
#	我们可以把任务分为计算密集型和IO密集型

# 	计算密集型任务的特点是要进行大量的计算，消耗CPU资源
# 	比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力
# 	这种计算密集型任务虽然也可以用多任务完成，但是任务越多
# 	花在任务切换的时间就越多,CPU执行任务的效率就越低
# 	所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数

# 	计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要
# 	Python这样的脚本语言运行效率很低，完全不适合计算密集型任务
# 	对于计算密集型任务，最好用C语言编写


# 	第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务
# 	这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成
# 	（因为IO的速度远远低于CPU和内存的速度）
# 	对于IO密集型任务，任务越多，CPU效率越高
# 	但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用

# 	IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少
# 	因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率
# 	对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言
# 	脚本语言是首选，C语言最差



#			异步IO

#	考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作
#	单进程单线程模型会导致别的任务无法并行执行
#	因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行

#	现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO
#	如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务
#	这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器
#	它在单核CPU上采用单进程模型就可以高效地支持多任务
#	在多核CPU上，可以运行多个进程（数量与CPU核心数相同）,充分利用多核CPU
#	由于系统总的进程数量十分有限，因此操作系统调度非常高效
#	用异步IO编程模型来实现多任务是一个主要的趋势


#	对应到Python语言，单线程的异步编程模型称为协程
#	有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程