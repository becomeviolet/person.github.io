#依赖项
from selenium import webdriver
from selenium.webdriver.common.by import By #容易忘
#创建实例对象，引入
driver = webdriver.Chrome()
#启动浏览器
driver.get("http://www.baidu.com")

#使用标签的ID属性进行定位 如唯一，但是动态id
driver.find_element(By.ID,"")
#使用标签的name属性进行定位
driver.find_element(By.NAME,'name的属性值')
#使用标签的class属性进行定位
driver.find_element(By.CLASS_NAME,'class的属性值')
#使用标签名进行定位
driver.find_element(By.TAG_NAME,'tag的属性值')
#使用超链接的名字进行定位
driver.find_element(By.LINK_TEXT,'超链接的名字?文本？')
#使用超链接的名字进行定位,支持模糊查询
driver.find_element(By.PARTIAL_LINK_TEXT,'超链接的名字')
#使用xpath定位语法进行定位
driver.find_element(By.XPATH,'xpath定位语法')
#使用css选择器定位语法进行定位
driver.find_element(By.CSS_SELECTOR,'css选择器语法')