'''
整合多个脚本至同一个测试用例中
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
from PO模式.v3.utils import DriverUtil, get_alert_msg
from PO模式.v4.index_page import IndexTask
from login_page import LoginTask

class TestLogin(object):
    '''登录测试类'''

    def setup_class(self):
        self.driver = DriverUtil.get_driver()#获取浏览器对象
        self.Index_task = IndexTask()#实例化首页业务层对象
        self.login_task = LoginTask()#实例化登录页面业务层对象

    def teardown_class(self):
        DriverUtil.quit_driver() #推出浏览器对象

    def setup(self):
        self.driver.get('http://127.0.0.1/')#打开首页
        self.Index_task.go_to_ligon()#跳转登录

    def teardown(self):
        pass

    def test_accout_does_not_exist(self):
        '''账号不存在测试方法'''
        #执行登录
        self.login_task.login_method('13811110001', '123456', '8888')
        msg = get_alert_msg()  # 获取弹窗信息
        print('错误信息：', msg)

    def test_wrong_password(self):
        '''密码错误测试方法'''
        #执行登录
        self.login_task.login_method('13800001111', 'error', '8888')
        msg = get_alert_msg()#获取弹窗信息
        print('错误信息：', msg)

if __name__ == '__main__':
    pytest.main(['-s', 'tpshop_login.py'])
