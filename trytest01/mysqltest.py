import mysql.connector

config={'host':'data-tt.curato.cn',			#配置信息以字典格式赋值
        'user':'so',
        'password':'leihou888',
        'port':3306 ,
        'database':'so-test',
        }

cnn=mysql.connector.connect(**config)       #登陆数据库
cursor=cnn.cursor()     #游标--->cursor   -->获取操作数据库的权限

#情况1：查询语句传参，元组传参
sql_1='select *   from    student where   name=%s'
data_1=('boom11',)
cursor.execute(sql_1,data_1)        #执行语句
result=cursor.fetchall()
#fetchall()把查询结果里的所有值都读取出来，相对fetchaone()只读取一条数据，fetchall()更好
print(result)

# #情况2：插入单组数据
# sql_2='insert  into    student(age,name)   values(%s,%s)'
# data_2=(10,'boom22')
# cursor.execute(sql_2,data_2)        #插入单组数据执行语句
# cursor.execute("commit")		#插入数据需加上该操作

# #情况3：插入多组数据，元组传参
# sql_3='insert  into    student(age,name)   values(%s,%s)'
# data_3=[(10,'boom55'),(11,'boom66')]
# cursor.executemany(sql_3,data_3)        #插入多组数据执行语句
# cursor.execute("commit")

# #情况4：插入多组数据，字典传参
# sql_4='insert  into    student(age,name)   values(%(age)s,%(name)s)'
# data_4=[{'age':22,'name':'boom33'},{'age':23,'name':'boom44'}]
# cursor.executemany(sql_4,data_4)        #插入多组数据执行语句
# cursor.execute("commit")

cursor.close()		#先关闭游标
cnn.close()			#再关闭数据库