import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class test_web(unittest.TestCase):

    def setUp(self) -> None:
        #设置不会自动退出
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach",True)

        self.driver = webdriver.Chrome(options=self.option)

        self.driver.get("http://v4.crmeb.net/admin/login")

    def test01(self):
        self.denglu()



    def denglu(self):
        #登录页面
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[基础_1]/div[2]/form/div[3]/div/button').click()
        #组合等待
        self.driver.implicitly_wait(10)
        time.sleep(1)
        #点掉图片
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/img').click()


if __name__ == "__main__":
    unittest.main()