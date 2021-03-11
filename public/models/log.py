import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config import setting
import configparser
import time, logging

# 获取配置文件
con = configparser.ConfigParser()
con.read(setting.LOG_DIR, encoding='UTF-8')
# 如果日志文件夹不存在，新建一个
if not os.path.exists(setting.LOG_DIR):
    os.mkdir(setting.LOG_DIR)


# 日志类
class Log():

    def __init__(self):
        # 设置日志文件名
        self.logName = os.path.join(setting.LOG_DIR, '%s.log'%format(time.strftime('%Y-%m-%d')))
        # 获取logger日志器
        self.logging = logging.getLogger()
        # 设置日志级别,等级比设置低的不会执行
        self.logging.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s] [%(filename)s|%(funcName)s] [line:%(lineno)d] %(levelname)-8s: %(message)s')

    # 日志执行函数
    def console(self,level, message):
        # 创建handler处理器,并添加日志文件输出
        handler = logging.FileHandler(self.logName, encoding='UTF-8')
        # 设置日志级别，未设置默认为warning
        handler.setLevel(logging.DEBUG)
        # 设置输出格式
        handler.setFormatter(self.formatter)
        self.logging.addHandler(handler)

        # 创建streamhandler，输出至控制台
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        streamHandler.setFormatter(self.formatter)
        self.logging.addHandler(streamHandler)

        if(level=='info'):
            self.logging.info(message)
        elif(level=='debug'):
            self.logging.debug(message)
        elif(level=='warning'):
            self.logging.warning(message)
        else:
            self.logging.error(message)

        handler.close()



    # 设置不同级别
    def info(self,message):
        self.console('info',message)

    def debug(self,message):
        self.console('debug',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)

