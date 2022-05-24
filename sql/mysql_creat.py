import pymysql
import yaml

with open('d:\pycode-learning\sql\config.yaml', 'r') as f:
    config = yaml.load(f,Loader=yaml.FullLoader)
    host = config['all_config']['host']
    port = config['all_config']['port']
    user = config['all_config']['user']
    password = config['all_config']['password']
    database = config['all_config']['database']

# 连接数据库
conn = pymysql.connect(host=host, port=port, user=user, password=password, charset='utf8', database=database)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
# sql = "CREATE DATABASE IF NOT EXISTS chng_project"  # 创建数据库
# sql = "DROP DATABASE IF EXISTS 数据库"     # 删库跑路
# sql = "DROP TABLE number"    # 删除表
sql = "create table number(id int primary key, number varchar(20), type varchar(30), name varchar(20))" # 创建编号表
# 执行sql语句
cursor.execute(sql)
# 关闭数据库连接
conn.close()