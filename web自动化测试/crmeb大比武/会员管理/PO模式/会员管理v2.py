import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest




class test_customer(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Edge()
        self.driver.get("http://139.9.209.241:8080/woniusales/")
        self.driver.maximize_window()

    def test_login(self):
        self.driver.find_element(By.ID, '''username''').send_keys('''admin''')
        self.driver.find_element(By.ID, '''password''').send_keys('''admin123''')
        self.driver.find_element(By.ID, '''verifycode''').send_keys('''0000''')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '''/html/body/div[4]/div/form/div[6]/button''').click()
        time.sleep(2)
        text1 = self.driver.find_element(By.XPATH, '''/html/body/div[2]/div/div[2]/ul[2]/li[1]/a''').text
        assert "管理员" in text1
        time.sleep(1)

    def test_add(self):
        self.driver.find_element(By.XPATH, '''//*[@id="navbar"]/ul[1]/li[5]/a''').click()
        time.sleep(1)
        self.driver.find_element(By.ID, '''customerphone''').send_keys('''19914665037''')
        self.driver.find_element(By.ID, '''customername''').clear()
        self.driver.find_element(By.ID, '''customername''').send_keys('''test_hzt''')
        Select1 = Select(self.driver.find_element(By.ID, '''childsex'''))
        Select1.select_by_visible_text('''女''')

        self.driver.find_element(By.ID, '''childdate''').click()
        self.driver.find_element(By.XPATH, '''/html/body/div[6]/div[3]/table/tbody/tr[3]/td[5]''').click()
        self.driver.find_element(By.ID, '''creditkids''').clear()
        self.driver.find_element(By.ID, '''creditkids''').send_keys('''85''')
        self.driver.find_element(By.ID, '''creditcloth''').clear()
        self.driver.find_element(By.ID, '''creditcloth''').send_keys('''85''')
        self.driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[1]''').click()
        # 已经有的信息
        try:
            # js1 = '''document.querySelector("body > div.bootbox.modal.fade.mydialog.in > div > div > div.modal-footer > button").click()'''
            # self.driver.execute_script(js1)
            # self.driver.execute_script(js1)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''').click()
        except:
            print("重复添加")
        time.sleep(1)

    def test_select(self):
        self.driver.find_element(By.ID, '''customerphone''').clear()
        self.driver.find_element(By.ID, '''customerphone''').send_keys('''19914665037''')
        time.sleep(1)
        self.driver.find_element(By.ID, '''customername''').clear()
        self.driver.find_element(By.ID, '''customername''').send_keys('''test_hzt''')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[3]''').click()
        time.sleep(2)
    
    def test_amend(self):
        self.driver.find_element(By.XPATH, '''//*[@id="customerlist"]/tr[1]/td[11]/a''').click()
        self.driver.find_element(By.XPATH, '''//*[@id="editBtn"]''').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''').click()
        time.sleep(2)


if __name__ == '__main__':
    suite1 = unittest.TestSuite()
    suite1.addTest(test_customer('test_login'))
    suite1.addTest(test_customer('test_add'))
    suite1.addTest(test_customer('test_select'))
    suite1.addTest(test_customer('test_amend'))
    runner = unittest.TextTestRunner()
    runner.run(suite1)