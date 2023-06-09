import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
#强制
time.sleep(1)

#创建实例
driver = webdriver.Chrome()

#隐式
driver.implicitly_wait(2)

#显示等待
WebDriverWait(driver,2)