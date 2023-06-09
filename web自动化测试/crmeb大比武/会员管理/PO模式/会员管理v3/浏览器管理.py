'''
公共方法模块：习惯命名utils
'''
from selenium import webdriver
from time import sleep
class DriverUtil(object):
    """浏览器对象管理类"""
    #说明：对象变量只需要在类定义内部使用，因此定义为私有
    __driver = None #浏览器对象变量初始化状态
    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        #说明：为了防止在同一次测试过程中，调用获取浏览器对象方法时
        #都会创建一个新的浏览器对象，因此有必要先判断对象是否存在，不存在时在创建！
        if cls.__driver is None:
            cls.__driver = webdriver.Edge()
            cls.__driver.get('http://139.9.209.241:8080/woniusales/')#项目地址
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver
    @classmethod
    def quit_driver(cls):
        """退出出浏览器对象方法"""
        #说明：必须保证浏览器对象存在，才能执行退出操作
        if cls.__driver:#等价于：if cls.__driver is not None:
            sleep(3)
            cls.__driver.quit()
            cls.__driver = None #保险手段：移除对象后，保留对象变量，以备下一次使用

if __name__ == '__main__':
    DriverUtil.get_driver()
    sleep(2)
    DriverUtil.quit_driver()
