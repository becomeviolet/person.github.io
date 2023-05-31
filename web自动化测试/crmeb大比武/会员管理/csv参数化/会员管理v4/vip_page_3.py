"""
登录页面
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from  浏览器管理 import DriverUtil
class vip_Page3(object):
    """登录对象层"""

    def __init__(self):
        """获取浏览器对象"""
        self.driver = DriverUtil.get_driver()
    
    def find_x1(self):
        return self.driver.find_element(By.XPATH, '''//*[@id="customerlist"]/tr[1]/td[11]/a''')
    
    def find_x2(self):
        return self.driver.find_element(By.XPATH, '''//*[@id="editBtn"]''')
    
    def find_x3(self):
        return self.driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''')
 
class vip_Handle3(object):
    """登录操作层"""

    def __init__(self):
        """获取对象层对象"""
        self.vip_page3 = vip_Page3()

    def CZ_x1(self):
        self.vip_page3.find_x1().click()
    
    def CZ_x2(self):
        self.vip_page3.find_x2().click()

    def CZ_x3(self):
        self.vip_page3.find_x3().click()

class vip_Task3(object):
    """登录业务层"""

    def __init__(self):
        """获取操作层对象"""
        self.vip_handle3 = vip_Handle3()

    def vip_method(self,):
        """登录方法"""
        self.vip_handle3.CZ_x1()
        self.vip_handle3.CZ_x2()
        time.sleep(1)
        self.vip_handle3.CZ_x3()
        time.sleep(2)

        
