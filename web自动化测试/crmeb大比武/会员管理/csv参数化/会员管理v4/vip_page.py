"""
登录页面
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from  浏览器管理 import DriverUtil
class vip_Page(object):
    """登录对象层"""

    def __init__(self):
        """获取浏览器对象"""
        self.driver = DriverUtil.get_driver()

    def find_vip_guanli(self):
        """定位会员管理"""
        return self.driver.find_element(By.XPATH, '''//*[@id="navbar"]/ul[1]/li[5]/a''')

    def find_phone(self):
        """定位手机号码方法"""
        return self.driver.find_element(By.ID, '''customerphone''')

    def find_vip_name(self):
        """定位会员昵称方法"""
        return self.driver.find_element(By.ID, '''customername''')

    def find_Select(self):
        """定位下拉框方法"""
        return Select(self.driver.find_element(By.ID, '''childsex''')) 
    
    def find_xxx1(self):
        """定位出生日期1"""
        return self.driver.find_element(By.ID, '''childdate''')
    
    def find_xxx2(self):
        """定位出生日期2"""
        return self.driver.find_element(By.XPATH, '''/html/body/div[6]/div[3]/table/tbody/tr[3]/td[5]''')
    
    def find_MYJF(self):
        """定位母婴积分"""
        return self.driver.find_element(By.ID, '''creditkids''')
    
    def find_TZJF(self):
        """定位童装积分""" 
        return self.driver.find_element(By.ID, '''creditcloth''')
    
    def find_XZ(self):
        """定位新增"""
        return self.driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[1]''')
    
    def find_chongfu(self):
        """定位重复"""
        return self.driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''')
    
class vip_Handle(object):
    """登录操作层"""

    def __init__(self):
        """获取对象层对象"""
        self.vip_page = vip_Page()

    def click_vip_guanli(self):
        """点击会员管理"""
        self.vip_page.find_vip_guanli().click()

    def input_phone(self, phone):
        """输入手机号"""
        self.vip_page.find_phone().send_keys(phone)

    def input_vip_name(self, name):
        """输入会员昵称"""
        self.vip_page.find_vip_name().clear()
        self.vip_page.find_vip_name().send_keys(name)

    def click_Select(self, sex):
        """操作下拉框"""
        self.vip_page.find_Select().select_by_visible_text(sex)
    
    def caozuo_Born(self):
        """操作出生日期"""
        self.vip_page.find_xxx1().click()
        self.vip_page.find_xxx2().click()

    def caozuo_MYJF(self, number1):
        """操作母婴积分"""
        self.vip_page.find_MYJF().clear()
        self.vip_page.find_MYJF().send_keys(number1)

    def caozuo_TZJF(self, number2):
        """操作童装积分"""
        self.vip_page.find_TZJF().clear()
        self.vip_page.find_TZJF().send_keys(number2)

    def click_XZ(self):
        """点击新增"""
        self.vip_page.find_XZ().click()

    def click_CF(self):
        """处理重复信息"""
        self.vip_page.find_chongfu().click()
        self.vip_page.find_chongfu().click()


class vip_Task(object):
    """登录业务层"""

    def __init__(self):
        """获取操作层对象"""
        self.vip_handle = vip_Handle()

    def vip_method(self, phone, name, sex, number1, number2):
        """登录方法"""
        #点击会员管理
        self.vip_handle.click_vip_guanli()
        #暂停
        time.sleep(2)
        #输入手机号
        self.vip_handle.input_phone(phone)
        #输入会员昵称
        self.vip_handle.input_vip_name(name)
        #操作下拉框
        self.vip_handle.click_Select(sex)
        #点击出生日期
        self.vip_handle.caozuo_Born()
        #操作母婴积分
        self.vip_handle.caozuo_MYJF(number1)
        #操作童装积分
        self.vip_handle.caozuo_TZJF(number2)
        #点击新增
        self.vip_handle.click_XZ()
        #页面变动暂停
        time.sleep(2)
        #已经有的信息
        try:
            self.vip_handle.click_CF()
        except:
            print("非重复添加")
        #页面变动暂停
        time.sleep(1)

        

  