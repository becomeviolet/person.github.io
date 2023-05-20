import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class test_web(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("http://139.196.167.227/admin/login")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div/div/input').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[3]/div/div[1]/div/div/input').send_keys('8')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[4]/div/button').click()
        time.sleep(3)

    def test_kefuhuihua(self):
        self.kefuhuihua()
        self.TianJiaFengLei()
        self.BianJi()
        self.ShanChu()

    def ShanChu(self):
        self.driver.find_element(By.XPATH, '''//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/div/a[2]''').click()
        self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/div/div/div[3]/button[2]/span''').click()
        time.sleep(2)

    def BianJi(self):
        self.driver.find_element(By.XPATH, '''//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/div/a[1]''').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[3]/div/div/div/textarea''').clear()
        self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[3]/div/div/div/textarea''').send_keys('''test123456''')
        self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/button''').click()
        try:
            self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/a/i''').click()
        except:
            print("正向")
        time.sleep(2)

    def TianJiaFengLei(self):
        self.driver.find_element(By.XPATH, '''//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div/button[2]/span''').click()
        self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[1]/div/div/div/div/input''').send_keys('''test''')
        time.sleep(1)
        self.driver.find_element(By.XPATH,'''/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/button''').click()
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/a/i''').click()
        except:
            print("正向")
        time.sleep(1)

    def kefuhuihua(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/li[5]/div').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/li[5]/ul/li[2]/span').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/ul/li/ul/li[5]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div/button[1]/span').click()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[1]/div/div/div/div[1]/div/i').click()
        self.driver.implicitly_wait(1)
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[1]/div/div/div/div[2]/ul[2]/li[4]').click()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[2]/div/div/div/textarea').send_keys(
            "test")
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[3]/div/div/div/textarea').send_keys(
            "test_123456")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '''/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/button''').click()
        try:
            self.driver.find_element(By.XPATH,'''/html/body/div[16]/div[2]/div/div/a/i''').click()
        except:
            print("正向")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()