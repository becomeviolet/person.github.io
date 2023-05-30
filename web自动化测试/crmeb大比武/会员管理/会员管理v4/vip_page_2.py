"""
登录页面
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from  浏览器管理 import DriverUtil
class vip_Page2(object):
    """登录对象层"""
    
    def __init__(self):
        """获取浏览器对象"""
        self.driver = DriverUtil.get_driver()
    
    def find_x1(self):
        return self.driver.find_element(By.ID, '''customerphone''')
    
    def find_x2(self):
        return self.driver.find_element(By.ID, '''customername''')
    
    def find_x3(self):
        return self.driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[3]''')
   
class vip_Handle2(object):
    """登录操作层"""

    def __init__(self):
        """获取对象层对象"""
        self.vip_page = vip_Page2()

    def CZ_x1(self, phone):
        self.vip_page.find_x1().clear()
        self.vip_page.find_x1().send_keys(phone)
    
    def CZ_x2(self, name):
        self.vip_page.find_x2().clear()
        self.vip_page.find_x2().send_keys(name)
    
    def CZ_x3(self):
        self.vip_page.find_x3().click()
    
class vip_Task2(object):
    """登录业务层"""

    def __init__(self):
        """获取操作层对象"""
        self.vip_handle = vip_Handle2()

    def vip_method(self, phone, name):
        """查询方法"""
        self.vip_handle.CZ_x1(phone)
        self.vip_handle.CZ_x2(name)
        time.sleep(2)
        self.vip_handle.CZ_x3()
        time.sleep(1)

   

        