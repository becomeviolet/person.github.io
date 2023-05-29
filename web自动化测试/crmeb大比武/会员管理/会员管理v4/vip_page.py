"""
登录页面
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from  浏览器管理 import DriverUtil
class vip_Page(object):
    """登录对象层"""
        # self.driver.find_element(By.XPATH, '''//*[@id="navbar"]/ul[1]/li[5]/a''').click()
        # time.sleep(1)
        # self.driver.find_element(By.ID, '''customerphone''').send_keys('''19914665037''')
        # self.driver.find_element(By.ID, '''customername''').clear()
        # self.driver.find_element(By.ID, '''customername''').send_keys('''test_hzt''')
        # Select1 = Select(self.driver.find_element(By.ID, '''childsex'''))
        # Select1.select_by_visible_text('''女''')

        # self.driver.find_element(By.ID, '''childdate''').click()
        # self.driver.find_element(By.XPATH, '''/html/body/div[6]/div[3]/table/tbody/tr[3]/td[5]''').click()
        # self.driver.find_element(By.ID, '''creditkids''').clear()
        # self.driver.find_element(By.ID, '''creditkids''').send_keys('''85''')
        # self.driver.find_element(By.ID, '''creditcloth''').clear()
        # self.driver.find_element(By.ID, '''creditcloth''').send_keys('''85''')
        # self.driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[1]''').click()
        # # 已经有的信息
        # try:
        #     time.sleep(2)
        #     self.driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''').click()
        # except:
        #     print("重复添加")
        # time.sleep(1)
    def __init__(self):
        """获取浏览器对象"""
        self.driver = DriverUtil.get_driver()

    def find_vip_guanli(self):
        """定位会员管理"""
        return self.driver.find_element(By.XPATH, '''//*[@id="navbar"]/ul[1]/li[5]/a''')
        #return self.driver.find_element(By.ID,'username')

    def find_phone(self):
        """定位手机号码方法"""
        return self.driver.find_element(By.ID, '''customerphone''')
        # return self.driver.find_element(By.ID,'password')

    def find_vip_name(self):
        """定位会员昵称方法"""
        return self.driver.find_element(By.ID, '''customername''')
        # return self.driver.find_element(By.ID,"verify_code")

    def find_Select(self):
        """定位下拉框方法"""
        return Select(self.driver.find_element(By.ID, '''childsex''')) 
        # return self.driver.find_element(By.NAME,'sbtbutton')

    def find_assert_text(self):
        """定位需要验证的text"""
        # return self.driver.find_element(By.ID, '''childdate''').click()


class vip_Handle(object):
    """登录操作层"""

    def __init__(self):
        """获取对象层对象"""
        self.login_page = vip_Page()

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

class vip_Task(object):
    """登录业务层"""

    def __init__(self):
        """获取操作层对象"""
        self.login_handle = vip_Handle()

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

  