import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import unittest

class test_customer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls,self) -> None:
        self.driver = webdriver.Edge()
        self.driver.get(url='w')
        self.driver.maximize_window()


    def test_login(self):
        pass
    
    def test_add(self):
        pass

    def test_select(self):
        pass

    def test_amend(self):
        pass

if __name__ == "__main__":
    suite1 = unittest.TestSuite()
    suite1.addTest(test_customer('test_login'))
    suite1.addTest(test_customer('test_add'))
    suite1.addTest(test_customer('test_select'))
    suite1.addTest(test_customer('test_amend'))
    runner = unittest.TextTestRunner()
    runner.run(suite1)
