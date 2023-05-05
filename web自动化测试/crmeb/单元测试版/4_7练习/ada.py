import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

class Web_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()



    def test01(self):
        self.driver.get("http://v4.crmeb.net/admin/login")
        #登录
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys("admin")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/div/div/div/input").send_keys("admin123")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[3]/div/div/div/div/input").send_keys("qa1")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/div/button").click()
        #暂停
        time.sleep(1)
        #获取文本内容
        assert "admin" in self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/span").text
        #点击商品
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/span").click()
        #暂停并点击商品管理
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/ul/li[1]/span").click()
        #暂停并点击添加商品
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/a/button/span").click()
        #输入商品名称
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/div/div/div/input").send_keys("test_name")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/div/div/div[1]/div/i").click()
        #暂停并选中
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/div/div/div[2]/ul[2]/li[6]").click()
        self.driver.find_element(By.XPATH,'''/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/div/div/div[1]/div/i''').click()
        #暂停并输入
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/div/div/div/div/input").send_keys("test_key")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/form/div[1]/div[4]/div/div/div/div/input").send_keys("test_test")
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/form/div[1]/div[5]/div/div/div/textarea").send_keys("test_商品简介")
        #暂停并点击商品封面图
        time.sleep(1)
        self.driver.execute_script("document.querySelector('#shopp-manager > div.ivu-mt.ivu-card.ivu-card-dis-hover > div > form > div:nth-child(1) > div:nth-child(6) > div > div > div > div > i').click()")


    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()