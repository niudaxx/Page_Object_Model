# @Time:2021/4/14 10:22
# @Author:testDa
# @File:excute_cases.py
# @Reason:

import unittest,datetime,os
from BeautifulReport import BeautifulReport
from config import setting


casePath = os.path.dirname(os.path.realpath(__file__))
discover = unittest.defaultTestLoader.discover(casePath, pattern='test*.py', top_level_dir=None)
time = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(time)
BeautifulReport(discover).report(description='测试报告', filename=filename, log_path=setting.REPORT_DIR)