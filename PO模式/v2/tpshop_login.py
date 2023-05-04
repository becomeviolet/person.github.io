'''
整合多个脚本至同一个测试用例中
'''
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class TestLogin(object):
    '''登录测试类'''

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def teardown_class(self):
        sleep(3)
        self.driver.quit()
    def setup(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get('http://127.0.0.1/')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        #返回原本页面
        self.driver.get('http://127.0.0.1/')
        #点击登录
        self.driver.find_element(By.LINK_TEXT,"登录").click()
    def teardown(self):
        # sleep(3)
        # self.driver.quit()
        pass

    def test_accout_does_not_exist(self):
        '''账号不存在测试方法'''

        # 点击首页的“登录”链接，进入登录页面
        # self.driver.find_element(By.LINK_TEXT, "登录").click()
        # 输入一个不存在的用户名
        self.driver.find_element(By.ID, 'username').send_keys('13811110001')
        # 输入密码
        self.driver.find_element(By.ID, "password").send_keys('123456')
        # 输入验证码
        self.driver.find_element(By.ID, 'verify_code').send_keys('8888')
        # 点击登录按钮
        self.driver.find_element(By.NAME, 'sbtutton').click()
        # 获取错误信息
        # 获取元素文本值
        sleep(2)
        msg = self.driver.find_element(By.CLASS_NAME, 'layui_layer_content').text
        print('错误信息：', msg)

    def test_wrong_password(self):
        '''密码错误测试方法'''

        # 点击首页的“登录”链接，进入登录页面
        # self.driver.find_element(By.LINK_TEXT, "登录").click()
        # 输入一个用户名
        self.driver.find_element(By.ID, 'username').send_keys('13811110000')
        # 输入错误密码
        self.driver.find_element(By.ID, "password").send_keys('error')
        # 输入验证码
        self.driver.find_element(By.ID, 'verify_code').send_keys('8888')
        # 点击登录按钮
        self.driver.find_element(By.NAME, 'sbtutton').click()
        # 获取错误信息
        # 获取元素文本值
        sleep(2)
        msg = self.driver.find_element(By.CLASS_NAME, 'layui_layer_content').text
        print('错误信息：', msg)

if __name__ == '__main__':
    pytest.main(['-s', 'tpshop_login_3.py'])
