#依赖项
from selenium import webdriver
# 创建实例
driver = webdriver.Chrome()
#启动浏览器
driver.get('http://www.baidu.com')

#窗口最大化
driver.maximize_window()
#窗口最小化
driver.minimize_window()
#全屏
driver.fullscreen_window()
#设置窗口大小，如720，720
driver.set_window_size(720,720)
