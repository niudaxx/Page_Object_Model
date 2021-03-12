import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from public.pageObj.basePage import base_page
from config import setting
from public.models.getyaml import getYaml
from time import sleep
testdata = getYaml(setting.ELEMENT_DIR + "\\" + 'login_element.yaml')


# 登陆页面
class login_page(base_page):
    # 用户名
    login_user_loc = (testdata.get_find_type(1), testdata.get_element_info(1))
    # 密码
    login_pwd_loc = (testdata.get_find_type(2), testdata.get_element_info(2))
    # 厂区
    login_comp_loc = (testdata.get_find_type(3), testdata.get_element_info(3))
    # 部门
    login_dept_loc = (testdata.get_find_type(4), testdata.get_element_info(4))
    # 登陆
    login_btn_loc = (testdata.get_find_type(5), testdata.get_element_info(5))

    # 输入用户名
    def login_user(self, userName):
        self.send_key(*self.login_user_loc, userName)

    # 输入密码
    def login_pwd(self, password):
        self.send_key(*self.login_pwd_loc, password)

    # 选择厂区
    def sel_comp(self, val):
        self.element_selected(*self.login_comp_loc,val)

    # 选择部门
    def sel_dept(self, val):
        self.element_selected(*self.login_dept_loc,val)

    # 点击登陆
    def login_check(self):
        self.onclick(*self.login_btn_loc)

    def _login(self,user,pwd,compval = 0,deptval = 0):
        self.login_user(user)
        sleep(1)
        self.login_pwd(pwd)
        sleep(1)
        self.sel_comp(compval)
        self.sel_dept(deptval)
        sleep(1)
        self.login_check()