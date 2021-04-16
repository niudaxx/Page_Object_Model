# @Time:2021/4/13 13:42
# @Author:testDa
# @File:test_case1.py
# @Reason:
from requestsCase.base_test import BaseTest
from public.models.getyaml import getYaml
from config import setting
from public.models.log import Log
import os
log = Log()

testData = getYaml(setting.REQUESTS_DIR + '/' + 'test_case1.yaml')
class TestCase1(BaseTest):


    def test_case1(self):
        url = testData.get_requestsParam_url(0)
        type = testData.get_requestsParam_type(0)
        data = testData.get_requestsParam_data(0)
        result = self.case_method(url=url,req_type=type,data=data,headers=self.session.headers,cookie=self.cookiejar.get_dict())
        self.assertIn(result,[{'hasFile':'Y'},{'hasFile':'N'}])

    def test_case2(self):
        url = testData.get_requestsParam_url(1)
        type = testData.get_requestsParam_type(1)
        data = testData.get_requestsParam_data(1)
        result = self.case_method(url=url, req_type=type, data=data, headers=self.session.headers,
                                  cookie=self.cookiejar.get_dict())
        print(result)

    def test_case3(self):
        url = testData.get_requestsParam_url(2)
        type = testData.get_requestsParam_type(2)
        data = testData.get_requestsParam_data(2)
        result = self.case_method(url=url, req_type=type, data=data, headers=self.session.headers,
                                  cookie=self.cookiejar.get_dict())
        print(result)


import unittest,datetime
from BeautifulReport import BeautifulReport
if __name__ == '__main__':
    casePath = os.path.dirname(os.path.realpath(__file__))
    discover = unittest.defaultTestLoader.discover(casePath,pattern='test*.py',top_level_dir=None)
    time = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    filename = '测试报告'+str(time)
    BeautifulReport(discover).report(description='测试报告',filename=filename,log_path=setting.REPORT_DIR)

    # runner = unittest.TextTestRunner()
    # runner.run(discover)