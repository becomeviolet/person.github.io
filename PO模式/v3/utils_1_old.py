'''
公共方法模块：习惯命名utils
'''
from selenium import webdriver
from time import sleep

class DriverUtil(object):
    """浏览器对象管理类"""
    driver = None #浏览器对象变量初始化状态

    def get_driver(self):
        """获取浏览器对象方法"""
        #说明：为了防止在同一次测试过程中，调用获取浏览器对象方法时
        #都会创建一个新的浏览器对象，因此有必要先判断对象是否存在，不存在时在创建！
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get('http://127.0.0.1/')
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        return self.driver

    def quit_driver(self):
        """推出浏览器对象方法"""
        #说明：必须保证浏览器对象存在，才能执行退出操作
        if self.driver:#等价于：if self.driver is not None:
            sleep(3)
            self.driver.quit()
            self.driver = None #保险手段：移除对象后，保留对象变量，以备下一次使用

if __name__ == '__main__':
    my_driver = DriverUtil()
    my_driver.get_driver()
    sleep(2)
    my_driver.quit_driver()
