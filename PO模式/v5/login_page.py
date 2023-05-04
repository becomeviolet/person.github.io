"""
登录页面
"""
from selenium.webdriver.common.by import By

from utils import DriverUtil
class LoginPage(object):
    """登录对象层"""

    def __init__(self):
        """获取浏览器对象"""
        self.driver = DriverUtil.get_driver()
        #说明：将元素的定位方法及特征值封装成属性，能够实现集中管理目标元素的的定位方法及特征值
        self.name = (By.ID, 'username')# 用户名
        self.pwd = (By.ID, 'password') #密码
        self.code = (By.ID, 'verify_code')#验证码
        self.btn = (By.NAME, 'sbtbutton')#登录按钮

    def find_username(self):
        """定位用户名方法"""
        # return self.driver.find_element(By.ID, 'username')
        return self.driver.find_element(self.name[0], self.name[1])

    def find_password(self):
        """定位密码方法"""
        # return self.driver.find_element(By.ID,'password')
        return self.driver.find_element(self.pwd[0], self.pwd[1])

    def find_verify_code(self):
        """定位验证码方法"""
        # return self.driver.find_element(By.ID, 'erify_code)
        return self.driver.find_element(self.code[0], self.code[1])

    def find_login_btn(self):
        """定位登录按钮方法"""
        # return self.driver.find_element(By.NAME,'sbtbutton')
        return self.driver.find_element(self.btn[0], self.btn[1])

class LoginHandle(object):
    """登录操作层"""

    def __init__(self):
        """获取对象层对象"""
        self.login_page = LoginPage()

    def input_username(self, name):
        """输入用户名方法"""
        # 说明：在执行输入操作前， 应该先执行清空操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(name)

    def input_password(self, pwd):
        """输入密码方法"""
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(pwd)

    def input_verify_code(self, code):
        """输入验证码方法"""
        self.login_page.find_verify_code().clear()
        self.login_page.find_verify_code().send_keys(code)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.login_page.find_login_btn().click()

class LoginTask(object):
    """登录业务层"""

    def __init__(self):
        """获取操作层对象"""
        self.login_handle = LoginHandle()

    def login_method(self, name, pwd, code):
        """登录方法"""
        #输入用户名
        self.login_handle.input_username(name)
        #输入密码
        self.login_handle.input_password(pwd)
        #输入验证码
        self.login_handle.input_verify_code(code)
        #点击登录按钮
        self.login_handle.click_login_btn().click()