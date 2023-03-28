import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#设置不自动关闭
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get("http://v4.crmeb.net/admin/login")
driver.execute_script('document.querySelector("#app > div > div.container.containerSamll > div.index_from.page-account-container.from-wh > form > div.pt10.ivu-form-item > div > button").click()')
#页面跳转，组合暂停
driver.implicitly_wait(10)
time.sleep(2)
#点掉图片
driver.execute_script('document.querySelector("#app > div > div.open-image > img").click()')
#结尾暂停
time.sleep(2)
