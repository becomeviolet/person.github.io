"""
登录页面
"""
import time
from selenium.webdriver.common.by import By

from  浏览器管理 import DriverUtil
class LoginPage(object):
    """登录对象层"""

    def __init__(self):
        """获取浏览器对象"""
        self.driver = DriverUtil.get_driver()

    def find_username(self):
        """定位用户名方法"""
        return self.driver.find_element(By.ID, '''username''')
        #return self.driver.find_element(By.ID,'username')

    def find_password(self):
        """定位密码方法"""
        return self.driver.find_element(By.ID, '''password''')
        # return self.driver.find_element(By.ID,'password')

    def find_verify_code(self):
        """定位验证码方法"""
        return self.driver.find_element(By.ID, '''verifycode''')
        # return self.driver.find_element(By.ID,"verify_code")

    def find_login_btn(self):
        """定位登录按钮方法"""
        return self.driver.find_element(By.XPATH, '''/html/body/div[4]/div/form/div[6]/button''') 
        # return self.driver.find_element(By.NAME,'sbtbutton')

    def find_assert_text(self):
        """定位需要验证的text"""
        return self.driver.find_element(By.XPATH, '''/html/body/div[2]/div/div[2]/ul[2]/li[1]/a''')

class LoginHandle(object):
    """登录操作层"""

    def __init__(self):
        """获取对象层对象"""
        self.login_page = LoginPage()

    def input_username(self, name):
        """输入用户名方法"""
        self.login_page.find_username().send_keys(name)

    def input_password(self, pwd):
        """输入密码方法"""
        self.login_page.find_password().send_keys(pwd)

    def input_verify_code(self, code):
        """输入验证码方法"""
        self.login_page.find_verify_code().send_keys(code)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.login_page.find_login_btn().click()
    
    def assert_text(self, text):
        """断言文本方法"""
        assert text in self.login_page.find_assert_text().text

class LoginTask(object):
    """登录业务层"""

    def __init__(self):
        """获取操作层对象"""
        self.login_handle = LoginHandle()

    def login_method(self, name, pwd, code, text):
        """登录方法"""
        #输入用户名
        self.login_handle.input_username(name)
        #输入密码
        self.login_handle.input_password(pwd)
        #输入验证码
        self.login_handle.input_verify_code(code)
        #点击登录按钮
        self.login_handle.click_login_btn()
        #跳转页面暂停
        time.sleep(2)
        #断言文本方法
        self.login_handle.assert_text(text)

