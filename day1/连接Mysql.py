import pymysql
conn = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='mysql') #连接属性
cursor = conn.cursor()
print(cursor.execute('select * from db')) #执行sql
print(cursor.fetchall()) #获取数据
print(cursor.execute('select * from help_category limit 0,1')) #执行sql