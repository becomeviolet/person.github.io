import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class kaida(unittest.TestCase):

    def setUp(self) -> None:
        self.driver= webdriver.Chrome()

    def test01(self):
        self.denglu()
        self.mubiao2()


    def denglu(self):
        #访问网址
        self.driver.get("http://v4.crmeb.net/admin/login")
        #点击登录
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/form/div[3]/div/button").click()
        time.sleep(3)
        #点掉图片
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/img").click()

    def mubiao1(self):
        #商品
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div/div[1]/ul/li[4]").click()
        time.sleep(1)
        #商品规格
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div/div[2]/ul/li[3]").click()
        time.sleep(1)
        #添加规格
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/button/span").click()
        time.sleep(1)
        #商品规格-添加新规格
        self.driver.find_element(By.XPATH,"//button[contains(@class,'ml95 mt10 ivu-btn ivu-btn-primary')]").click()
        #三值输入
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder='请输入标题名称']").send_keys("ada")
        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入规格']").send_keys("ada")
        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入规格值']").send_keys("ada")
        #确认输入
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, "//div[@class='ivu-col ivu-col-span-2']/button/span").click()
        #确认
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, "//div[@class='ivu-modal-footer']/div/button/span").click()
        # 模糊搜索
        self.driver.implicitly_wait(2)
        text1 = self.driver.find_element(By.XPATH,"//span[text()='保存成功']").text
        assert "保存成功" in text1

    def mubiao2(self):
        #商品
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div/div[1]/ul/li[4]").click()
        #商品评论
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div/div[2]/ul/li[4]/span").click()
        # 添加自评
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/button/span").click()
        #打开商品选项卡
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//i[@class="ivu-icon ivu-icon-ios-add"]').click()
        #选择
        self.driver.implicitly_wait(10)
        time.sleep(1)
        js1 ='document.querySelector("#app > div > div.ivu-table-wrapper > div.ivu-table.ivu-table-default > div.ivu-table-body.ivu-table-overflowY.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td.ivu-table-column-vpp1bU.ivu-table-column-center > div > div > label > span > input").click()'
        self.driver.execute_script(js1)




    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()