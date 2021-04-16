# @Time:2021/4/14 14:02
# @Author:testDa
# @File:testRunner.py
# @Reason:

import unittest,datetime,os
from BeautifulReport import BeautifulReport
from config import setting

casePath = os.path.dirname(os.path.realpath(__file__))
discover = unittest.defaultTestLoader.discover(casePath, pattern='testDemo.py', top_level_dir=None)
time = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(time)
BeautifulReport(discover).report(description='测试报告', filename=filename, log_path=setting.REPORT_DIR)


# from public.models import driver
# from selenium.webdriver.support.ui import Select
# from time import sleep
# dr = driver.brower()
#
# dr.get('http://localhost:8080/sisqp-web/')
# dr.find_element_by_id('userName').send_keys('luoxiaohong')
# dr.find_element_by_id('j_password').send_keys('f')
# Select(dr.find_element_by_id('departmentId')).select_by_index(1)
# sleep(5)
# dr.quit()