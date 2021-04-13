# @Time:2021/4/13 13:10
# @Author:testDa
# @File:base_test.py
# @Reason:

import unittest,os
import requests

class BaseTest(unittest.TestCase):

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()
        cls.session.post(url='http://localhost:8080/sisqp-web/j_spring_security_check',
                          data={'j_username': 'admin_1_12', 'userName': 'admin', 'j_password': 'f', 'companyId': '1',
                                'departmentId': '12'})
        cls.cookiejar = cls.session.cookies


    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass


if __name__ == '__main__':
    # 测试用例路径
    case_path = os.path.dirname(os.path.realpath(__file__))
    # 加载test.py文件，TestCase到TestSuite集合中，返回一个TestSuite实例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*_test.py", top_level_dir=None)
    print(discover)
    # 实例化runner
    runner = unittest.TextTestRunner()
    # 调用实例run方法
    runner.run(discover)
