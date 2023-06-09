#依赖项
from selenium import webdriver
#创建实例
driver = webdriver.Chrome()
#启动浏览器
driver.get('http://www.baidu.com')

#进入下一页
driver.forward()
#返回上一页
driver.back()
#刷新网页
driver.refresh()
