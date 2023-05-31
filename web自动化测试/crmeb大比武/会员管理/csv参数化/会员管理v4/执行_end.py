'''
整合多个脚本至同一个测试用例中
'''
import unittest

from login_page_end import LoginTask
from vip_page import vip_Task
from vip_page_2 import vip_Task2
from vip_page_3 import vip_Task3

from 浏览器管理 import DriverUtil

class test_customer(unittest.TestCase):
    '''登录测试类'''
    @classmethod
    def setUpClass(self) -> None:
        self.driver = DriverUtil.get_driver()#获取浏览器对象
        self.login_task = LoginTask()#实例化登录页面业务层对象
        self.vip_task = vip_Task()#实例化会员管理页面业务层对象
        self.vip_task2 = vip_Task2()#
        self.vip_task3 = vip_Task3()


    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver() #退出浏览器对象

    def test_login(self):
        """登录页方法"""
        self.login_task.login_method('''admin''', '''admin123''', '''0000''', '''管理员''')

    def test_add(self):
        """添加会员"""
        self.vip_task.vip_method('19914665037', 'test_hzt', '女', '85', '85')

    def test_select(self):
        """查询会员"""
        self.vip_task2.vip_method('19914665037', 'test_hzt')
    
    def test_amend(self):
        self.vip_task3.vip_method()
        

if __name__ == '__main__':
    suite1 = unittest.TestSuite()
    suite1.addTest(test_customer('test_login'))
    suite1.addTest(test_customer('test_add'))
    suite1.addTest(test_customer('test_select'))
    suite1.addTest(test_customer('test_amend'))
    runner = unittest.TextTestRunner()
    runner.run(suite1)
