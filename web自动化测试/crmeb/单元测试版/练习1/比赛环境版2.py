import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class kaida(unittest.TestCase):
    def SheZhi(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)

    def setUp(self) -> None:
        self.SheZhi()
        self.driver= webdriver.Chrome(options=self.option)


    def test01(self):
        self.denglu()

        self.mubiao2()


    def denglu(self):
        #访问网址
        self.driver.get("http://v4.crmeb.net/admin/login")
        #使浏览器最大化尺寸
        self.driver.maximize_window()
        #点击登录
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[基础_1]/div[2]/form/div[3]/div/button").click()
        #等待页面刷新结束
        time.sleep(3)
        #点掉图片
        self.driver.find_element(By.XPATH, "/html/body/div[基础_1]/div/div[3]/img").click()

    def mubiao1(self):
        #点击商品
        self.driver.find_element(By.XPATH, "/html/body/div[基础_1]/div/div[基础_1]/div[基础_1]/div/div/div[基础_1]/ul/li[4]").click()
        #等待加载
        time.sleep(1)
        #点击商品规格
        self.driver.find_element(By.XPATH, "/html/body/div[基础_1]/div/div[基础_1]/div[基础_1]/div/div/div[2]/ul/li[3]").click()
        #等待加载
        time.sleep(1)
        #点击添加规格
        self.driver.find_element(By.XPATH,"/html/body/div[基础_1]/div/div[2]/div[2]/div/div[2]/div[基础_1]/div/div/form/div/div[2]/button/span").click()
        #等待加载
        time.sleep(1)
        #商品规格-添加新规格
        self.driver.find_element(By.XPATH,"//button[contains(@class,'ml95 mt10 ivu-btn ivu-btn-primary')]").click()
        #隐式等待
        self.driver.implicitly_wait(1)
        #三值输入
        self.driver.find_element(By.XPATH,"//input[@placeholder='请输入标题名称']").send_keys("test_title")
        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入规格']").send_keys("test_GuiGe")
        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入规格值']").send_keys("test_GuiGeZhi")
        #隐式等待
        self.driver.implicitly_wait(1)
        #确认输入
        self.driver.find_element(By.XPATH, "//div[@class='ivu-col ivu-col-span-2']/button/span").click()
        #隐式等待
        self.driver.implicitly_wait(1)
        #确认
        self.driver.find_element(By.XPATH, "//div[@class='ivu-modal-footer']/div/button/span").click()
        #等待
        time.sleep(2)
        # 模糊搜索
        text1 = self.driver.find_element(By.XPATH,"//span[text()='保存成功']").text
        #断言是否出现保存成功
        assert "保存成功" in text1

    def mubiao2(self):
        #商品
        self.driver.find_element(By.XPATH, "/html/body/div[基础_1]/div/div[基础_1]/div[基础_1]/div/div/div[基础_1]/ul/li[4]").click()
        #等待
        time.sleep(2)
        #商品评论
        self.driver.find_element(By.XPATH, "/html/body/div[基础_1]/div/div[基础_1]/div[基础_1]/div/div/div[2]/ul/li[4]/span").click()
        #等待
        time.sleep(1)
        #添加自评
        self.driver.find_element(By.XPATH,"/html/body/div[基础_1]/div/div[2]/div[2]/div/div[2]/div[基础_1]/div[2]/div/div[基础_1]/div/button/span").click()
        #等待
        time.sleep(1)
        #打开商品选项卡
        self.driver.find_element(By.XPATH,'//i[@class="ivu-icon ivu-icon-ios-add"]').click()
        #等待
        time.sleep(3)
        #定位与选择iframe
        self.iframe1 = self.driver.find_elements(By.XPATH,'//iframe')
        self.driver.switch_to.frame(self.iframe1[0])
        #等待
        time.sleep(1)
        #选择图片输入项
        self.driver.find_element(By.XPATH,'/html/body/div[基础_1]/div/div[基础_1]/div[基础_1]/div[2]/table/tbody/tr[基础_1]/td[基础_1]/div/div/label/span/input').click()
        #退出iframe
        self.driver.switch_to.default_content()
        #等待
        self.driver.implicitly_wait(10)
        time.sleep(1)
        #用户头像
        self.driver.find_element(By.XPATH,'//span[text()="用户头像"]/../../div/div/div/div/i').click()
        #等待
        time.sleep(2)
        #定位与选择iframe
        self.iframe2 = self.driver.find_elements(By.XPATH, '//iframe')
        self.driver.switch_to.frame(self.iframe2[0])
        #js定位选择图片
        self.driver.execute_script(script='document.querySelector("#app > div > div > div > div.colLeft.ivu-col.ivu-col-span-xs-24.ivu-col-span-sm-18.ivu-col-span-md-18.ivu-col-span-lg-18.ivu-col-span-xl-18 > div > div.pictrueList.acea-row > div > div.acea-row.mb10 > div:nth-child(基础_1) > img").click()')
        #确定选中图片
        self.driver.find_element(By.XPATH,'/html/body/div[基础_1]/div/div/div/div[2]/div/div[基础_1]/div/button[基础_1]/span').click()
        #退出iframe
        self.driver.switch_to.default_content()
        #等待
        time.sleep(2)
        #两个输入框输入
        self.driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名称"]').send_keys("test_hzt")
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']").send_keys("test_goodgood")
        #两个打分选择
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']/../../../../../div[5]/div/div/div/div[5]").click()
        self.driver.find_element(By.XPATH,'//textarea[@placeholder="请输入评价文字"]/../../../../../div[6]/div/div/div/div[5]').click()
        #等待
        time.sleep(1)
        #评价图片
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']/../../../../../div[7]/div/div/div/div/div/i").click()
        #定位并选择iframe
        self.iframe3 = self.driver.find_elements(By.XPATH,"//iframe")
        self.driver.switch_to.frame(self.iframe3[0])
        #js定位选择图片
        self.driver.execute_script(script='document.querySelector("#app > div > div > div > div.colLeft.ivu-col.ivu-col-span-xs-24.ivu-col-span-sm-18.ivu-col-span-md-18.ivu-col-span-lg-18.ivu-col-span-xl-18 > div > div.pictrueList.acea-row > div > div.acea-row.mb10 > div:nth-child(基础_1) > img").click()')
        self.driver.find_element(By.XPATH,'/html/body/div[基础_1]/div/div/div/div[2]/div/div[基础_1]/div/button[基础_1]/span').click()
        #退出iframe
        self.driver.switch_to.default_content()
        #等待
        time.sleep(2)
        #评论时间
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']/../../../../../../../form/div/div[8]/div/div/div").click()
        #等待
        time.sleep(2)
        #上个月
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']/../../../../../../../form/div/div[8]/div/div/div/div[2]/div/div/div/div/span[2]").click()
        #等待
        time.sleep(2)
        #选择日期
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']/../../../../../../../form/div/div[8]/div/div/div/div[2]/div/div/div/div[2]/div/span[17]").click()
        #等待
        time.sleep(2)
        #确定
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']/../../../../../../../form/div/div[8]/div/div/div/div[2]/div/div/div/div[4]/button[3]").click()
        #等待
        time.sleep(2)
        #提交
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='请输入评价文字']/../../../../../../../button").click()
        time.sleep(1)
        #模糊搜索
        text2 = self.driver.find_element(By.XPATH, "//span[text()='保存成功']").text
        #断言是否保存成功
        assert "保存成功" in text2
    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()