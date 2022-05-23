import logging

# 打印日志级别
def test():
    # 设置日志级别，默认为warning。
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')

# 将日志信息记录到文件
def save_to_file():
    logging.basicConfig(filename='F:/example.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

test()