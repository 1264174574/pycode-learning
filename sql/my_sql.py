import pymysql

# 连接数据库
conn = pymysql.connect( host="112.124.17.220",port=3306,user="root",password="lXX15703821212~",charset='utf8', database='chng_project')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
# sql = "CREATE DATABASE IF NOT EXISTS chng_project"  # 创建数据库
# sql = "DROP DATABASE IF EXISTS 数据库"     # 删库跑路
sql = cursor.execute("create table mun_table(id int(11) primary key auto_increment, number varchar(20), type varchar(30))")  # 创建编号表
# 执行sql语句
cursor.execute(sql)
# 关闭数据库连接
conn.close()