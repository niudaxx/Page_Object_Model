from selenium import webdriver
import configparser
# 根据配置文件的浏览器，获取webdriver
from config import setting
from public.models.log import Log

log = Log()
def brower():
    # 获取浏览器名
    try:
        con = configparser.ConfigParser()
        con.read(setting.SYSCONFIG_DIR, encoding='UTF-8')
        browerName = con.get('webdriver', 'BROWER_NAME')
        browerPath = con.get('webdriver', 'DRIVER_PATH_CHROME')
        if browerName=='CHROME':
            driver = webdriver.Chrome(browerPath)
            return driver
        else:
            log.error('目前只支持chrome浏览器')
    except Exception as ex:
        print("webdriver获取异常---->{0}".format(ex))
        log.error("webdriver获取异常---->{0}".format(ex))

