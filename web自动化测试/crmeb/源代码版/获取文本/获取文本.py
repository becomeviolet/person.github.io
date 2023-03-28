import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#设置不自动关闭
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("http://v4.crmeb.net/admin/login")
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/form/div[3]/div/button').click()
#页面跳转，组合暂停
driver.implicitly_wait(10)
time.sleep(2)
#点掉图片
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/img').click()

#driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div/div/div[5]/div/a/span').click()
driver.implicitly_wait(10)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div/div[1]/ul/li[4]").click()
driver.implicitly_wait(10)
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div/div/div[2]/ul/li[3]/span").click()
#结尾暂停
time.sleep(2)

text=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[3]/div/span').text
assert 'ada' in text
