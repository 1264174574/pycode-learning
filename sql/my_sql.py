import pymysql

# 连接数据库
conn = pymysql.connect( host="112.124.17.220",port=3306,user="root",password="lXX15703821212~",charset='utf8')   
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
sql = "CREATE DATABASE IF NOT EXISTS bianhao"
# 执行sql语句
cursor.execute(sql)
# 关闭数据库连接
conn.close()