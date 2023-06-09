from selenium import  webdriver
from selenium.webdriver.common.by import By
#创建实例对象，引入
driver = webdriver.Chrome()
#启动浏览器
driver.get("http://www.baidu.com")

driver.find_element(By.XPATH).send_keys()
driver.find_element(By.XPATH).click()
driver.find_element(By.XPATH).clear()