import time
import unittest

from  selenium import webdriver
from selenium.webdriver.common.by import By


class Baidu_Page(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.input_element = (By.ID,"kw")
        self.buttton_element = (By.ID,'su')

    def goto_baidu(self, url):
        self.driver.get(url)

    def test_search(self, url, kw):
        self.goto_baidu(url)
        self.driver.find_element(*self.input_element).send_keys(kw)
        self.driver.find_element(*self.buttton_element).click()

        time.sleep(5)

class TestBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.baiduPage = Baidu_Page()

    def test_search(self):
        self.baiduPage.test_search('http://www.baidu.com', 'selenium')

    if __name__ == '__main__':
        unittest.main()
