#					Python --- Mysql

#	MySQL是Web世界中使用最广泛的数据库服务器
#	SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用
#	而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite

#	此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB

#	首先，确保你的电脑上安装了mysql服务，下载mysql到官网就行，再次不做过多叙述
#	此外，安装mysql驱动
#	MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
$ pip install mysql-connector-python --allow-external mysql-connector-python

#	如果上面的命令安装失败，可以试试另一个驱动：
$ pip install mysql-connector

#	我们演示如何连接到MySQL服务器的test数据库：

import mysql.connector 		# 首先导入mysql驱动
conn = mysql.connector.connect(user = 'root', password = 'password', database = 'test')	# 设置口令
cursor = conn.cursor()
#	创建user表：
cursor.excute('CREATE TABLE user (id varchar(20) PRIMARY KEY, name varchar(30))')
#	插入一条记录，注意mysql的占位符是%s:
cursor.excute('INSERT INTO user (id, name) value(%s, %s)', ['1', 'kyle'])
cursor.rowcount		# 查看是否插入了数据

conn.commit()		# 提交事物
cursor.close()

#	运行查询：
cursor = conn.cursor()
cursor.excute('SELECT * FROM user WHERE id = (%s)', ('1',))
result = cursor.fetchall()
cursor.close()
conn.close()