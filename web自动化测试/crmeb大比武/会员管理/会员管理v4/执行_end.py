'''
整合多个脚本至同一个测试用例中
'''
import unittest
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page_end import LoginTask
from selenium.webdriver.support.select import Select


from 浏览器管理 import DriverUtil

class test_customer(unittest.TestCase):
    '''登录测试类'''
    @classmethod
    def setUpClass(self) -> None:
        self.driver = DriverUtil.get_driver()#获取浏览器对象
        # self.Index_task = IndexTask()#实例化首页业务层对象
        self.login_task = LoginTask()#实例化登录页面业务层对象

    def teardown_class(self):
        DriverUtil.quit_driver() #退出浏览器对象

    def setup(self):
        pass

    def teardown(self):
        pass

    # def test_accout_does_not_exist(self):
    #     '''账号不存在测试方法'''
    #     #执行登录
    #     self.login_task.login_method('13811110001', '123456', '8888')
    #     msg = get_alert_msg()  # 获取弹窗信息
    #     print('错误信息：', msg)

    # def test_wrong_password(self):
    #     '''密码错误测试方法'''
    #     #执行登录
    #     self.login_task.login_method('13800001111', 'error', '8888')
    #     msg = get_alert_msg()#获取弹窗信息
    #     print('错误信息：', msg)

    def test_login(self):
        # self.driver.find_element(By.ID, '''username''').send_keys('''admin''')
        # self.driver.find_element(By.ID, '''password''').send_keys('''admin123''')
        # self.driver.find_element(By.ID, '''verifycode''').send_keys('''0000''')
        self.login_task.login_method('''admin''', '''admin123''', '''0000''', '''管理员''')
  
        # time.sleep(1)
        # self.driver.find_element(By.XPATH, '''/html/body/div[4]/div/form/div[6]/button''').click()
        # time.sleep(2)
        # text1 = self.driver.find_element(By.XPATH, '''/html/body/div[2]/div/div[2]/ul[2]/li[1]/a''').text
        # assert "管理员" in text1
        # time.sleep(1)

    # def test_add(self):
    #     self.driver.find_element(By.XPATH, '''//*[@id="navbar"]/ul[1]/li[5]/a''').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.ID, '''customerphone''').send_keys('''19914665037''')
    #     self.driver.find_element(By.ID, '''customername''').clear()
    #     self.driver.find_element(By.ID, '''customername''').send_keys('''test_hzt''')
    #     Select1 = Select(self.driver.find_element(By.ID, '''childsex'''))
    #     Select1.select_by_visible_text('''女''')

    #     self.driver.find_element(By.ID, '''childdate''').click()
    #     self.driver.find_element(By.XPATH, '''/html/body/div[6]/div[3]/table/tbody/tr[3]/td[5]''').click()
    #     self.driver.find_element(By.ID, '''creditkids''').clear()
    #     self.driver.find_element(By.ID, '''creditkids''').send_keys('''85''')
    #     self.driver.find_element(By.ID, '''creditcloth''').clear()
    #     self.driver.find_element(By.ID, '''creditcloth''').send_keys('''85''')
    #     self.driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[1]''').click()
    #     # 已经有的信息
    #     try:
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''').click()
    #     except:
    #         print("重复添加")
        # time.sleep(1)

    # def test_select(self):
    #     self.driver.find_element(By.ID, '''customerphone''').clear()
    #     self.driver.find_element(By.ID, '''customerphone''').send_keys('''19914665037''')
    #     time.sleep(1)
    #     self.driver.find_element(By.ID, '''customername''').clear()
    #     self.driver.find_element(By.ID, '''customername''').send_keys('''test_hzt''')
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[3]''').click()
    #     time.sleep(2)
    
    # def test_amend(self):
    #     self.driver.find_element(By.XPATH, '''//*[@id="customerlist"]/tr[1]/td[11]/a''').click()
    #     self.driver.find_element(By.XPATH, '''//*[@id="editBtn"]''').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''').click()
    #     time.sleep(2)

if __name__ == '__main__':
    # suite1 = unittest.TestSuite()
    # suite1.addTest(test_customer('test_login'))
    # #suite1.addTest(test_customer('test_add'))
    # # suite1.addTest(test_customer('test_select'))
    # # suite1.addTest(test_customer('test_amend'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite1)
    unittest.main()
