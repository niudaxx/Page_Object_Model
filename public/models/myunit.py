from .driver import brower
import unittest


# 所有unittest父类，添加类前置、后置方法
class my_unit(unittest.TestCase):

    # 类加前执行
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = brower()
        # 隐式等待
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # 类执行完后执行
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
