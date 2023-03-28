import time
import unittest
from selenium import webdriver

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
        self.driver.execute_script('document.querySelector("#app > div > div.container.containerSamll > div.index_from.page-account-container.from-wh > form > div.pt10.ivu-form-item > div > button").click()')
        #组合等待
        self.driver.implicitly_wait(10)
        time.sleep(1)
        #点掉图片
        self.driver.execute_script('document.querySelector("#app > div > div.open-image > img").click()')


if __name__ == "__main__":
    unittest.main()