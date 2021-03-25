import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import setting
import configparser

# 获取登陆地址
con = configparser.ConfigParser()
con.read(setting.SYSCONFIG_DIR, encoding='UTF-8')
login_url = con.get('url', 'URL')

from public.models.log import Log

log = Log()

from selenium import webdriver


# 基础类
class base_page():

    def __init__(self, webderver, base_url=login_url, parent=None):
        self.driver = webderver
        # self.driver = webdriver.Chrome();
        self.base_url = base_url
        self.timeout = 10
        self.parent = parent

    # 根据地址访问
    def _open(self, url):
        url = self.base_url + "/" + url
        self.driver.get(url)

    # 获取元素定位
    def find_element(self, loc):
        try:
            # 显示等待
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            log.error('未找到页面元素%s' % loc)

    # 获取元素集合
    def find_elements(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_elements(*loc)
        except:
            log.error('未找到页面元素集合%s' % loc)

    # 文本框输入
    def send_key(self, loc, keys, clear_input=True):
        try:
            element = self.find_element(loc)
            if clear_input:
                element.clear()
            element.send_keys(keys)
        except Exception as ex:
            log.error('输入文件失败----->%s' % ex)

    # 点击元素
    def onclick(self, loc):
        try:
            element = self.find_element(loc)
            element.click()
        except Exception as ex:
            log.error('元素点击失败----->%s' % ex)

    # frame表单切换
    def switch_frame(self, loc):
        try:
            return self.driver.switch_to_frame(loc)
        except Exception as ex:
            log.error('未找到frame----->%s' % ex)

    # 子窗口切换
    def switch_windows(self, loc):
        try:
            return self.driver.switch_to_window(loc)
        except Exception as ex:
            log.error('未找到子窗口------>%s' % ex)

    # alert弹出框
    def switch_alert(self, loc):
        try:
            return self.driver.switch_to_alert(loc)
        except Exception as ex:
            log.error('未找到alert------>%' % ex)

    # 下拉框选择
    def element_selected(self, loc, val, sel_type='index'):
        try:
            element = Select(self.find_element(loc))
            if sel_type.__eq__('index'):
                element.select_by_index(val)
            elif sel_type.__eq__('value'):
                element.select_by_value(val)
            else:
                element.select_by_visible_text(val)
        except Exception as ex:
            log.error('未找到下拉框------>%' % ex)