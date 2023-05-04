"""
首页页面
"""
from selenium.webdriver.common.by import By

from utils import DriverUtil
class IndexPage(object):
    """首页对象层"""
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_login(self):
        """定位登录方法"""
        #self.driver = DriverUtil.get_driver()
        return self.driver.find_element(By.LINK_TEXT, "登录")

class IndexHandle(object):
    """首页操作层"""

    def __init__(self):
        """获取对象层对象"""
        self.index_page = IndexPage

    def click_login(self):
        """点击登录方法"""
        # element = IndexPage()
        self.indx_page.find_login().click()

class IndexTask(object):
    """首页业务层"""
    def __init__(self):
        """获取操作层对象"""
        self.index_handle = IndexHandle()

    def go_to_ligon(self):
        """跳转登录页面方法"""
        self.index_handle.click_login()

