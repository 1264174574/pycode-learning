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
    logging.basicConfig(filename='logger.log', level=logging.INFO)
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')

save_to_file()