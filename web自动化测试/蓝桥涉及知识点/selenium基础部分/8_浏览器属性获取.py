from selenium import  webdriver
from selenium.webdriver.common.by import By
#创建实例对象，引入
driver = webdriver.Chrome()
#启动浏览器
driver.get("http://www.baidu.com")
#获取当前url
driver.current_url
#获取当前句柄
driver.current_window_handle
#获取当前网页标题
driver.title

