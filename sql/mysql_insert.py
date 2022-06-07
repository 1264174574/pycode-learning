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

#插入sql语句
sql='''
    insert into number(id,number,type,name) values(%s,%s,%s,%s)
'''
#把数据以列表形式批量插入
add_data_list=[('1893','安全排查通知-220606-1893',"Confluence远程代码执行漏洞","li")]

try:
    #执行sql语句
    cursor.executemany(sql,add_data_list)
    #提交事务
    conn.commit()
    for i in range(len(add_data_list)):
        print('插入数据成功:{}'.format(add_data_list[i]))

except Exception as e:
    print(e)
    #如果出现异常，回滚
    conn.rollback()
    print('插入多条数据失败')
finally:
    #关闭数据库连接
    conn.close()
