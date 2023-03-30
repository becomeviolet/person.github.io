import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

class SearchCourseTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls)-> None:
        opt = Options()
       # opt.add_argument('--no-sandbox')
        service = Service("D:\\software\\chromedriver_win32\\chromedriver.exe")
        cls.driver = webdriver.Chrome(chrome_options=opt, service=service)
        cls.driver.get("http://lanqiao.cn")
        
    def test_login(self)->None:
        #点击首页登录按钮
        self.driver.find_element(By.CSS_SELECTOR,".signin").click()
        #点击手机号登录
        self.driver.find_element(By.CSS_SELECTOR,".cursor-pointer > span").click()
        #点击账户输入框并输入账号
        self.driver.find_element(By.CSS_SELECTOR,".ant-form-item-children > .ant-input").click()
        self.driver.find_element(By.CSS_SELECTOR,".ant-form-item-children > .ant-input").send_keys("123456")
        #点击密码输入框并输入密码
        self.driver.find_element(By.CSS_SELECTOR,".ant-input-affix-wrapper > .ant-input").click()
        self.driver.find_element(By.CSS_SELECTOR,".ant-input-affix-wrapper > .ant-input").send_keys("123456")
        #点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR,".mb-32px > .\\!text-18px").click()
        time.sleep(2)
        #获取登录后的用户名作为预期结果
        title = self.driver.find_element(By.CSS_SELECTOR,"div>span.name").text
        
        assert "123456" in title
        time.sleep(2)
        
    def test_search(self)->None: 
        # 在搜索输入框中输入 selenium
        
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[1]/form/input').send_keys("selenium")
		# 点击 搜索按钮
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[1]/form/button').click()
        time.sleep(2)
		# 关掉广告弹窗
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/div/img").click()
        time.sleep(2)
		# 打开 Python 自动化测试实战 课程
        self.driver.find_element(By.XPATH,"//*[@id=\"__layout\"]/div/div[3]/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/a/div/div[1]/div[1]/img").click()
        time.sleep(2)
        
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
	
		# 获取课程名称作为断言的预期结果
        title = self.driver.find_element(By.XPATH,"//*[@id=\"__layout\"]/div/div[3]/div[1]/div/div/div[1]/div[2]/div/div/section[1]/div/div[1]/div[1]/div/h1").text
        
        assert "Python 自动化测试实战" in title
        
    @classmethod
    def tearDownClass(cls)->None:
        cls.driver.quit()
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SearchCourseTest("test_login"))
    suite.addTest(SearchCourseTest("test_search"))
    unittest.TextTestRunner().run(suite)
  
  