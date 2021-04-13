# @Time:2021/4/13 13:42
# @Author:testDa
# @File:test_case1.py
# @Reason:
from requestsCase.base_test import BaseTest
from public.models.getyaml import getYaml
from config import setting


testData = getYaml(setting.REQUESTS_DIR + '/' + 'test_case1.yaml')
class TestCase1(BaseTest):


    def test_case1(self):
        url = testData.get_requestsParam_url(0)
        type = testData.get_requestsParam_type(0)
        data = testData.get_requestsParam_data(0)
        result = self.case_method(url=url,req_type=type,data=data,headers=self.session.headers,cookie=self.cookiejar.get_dict())

