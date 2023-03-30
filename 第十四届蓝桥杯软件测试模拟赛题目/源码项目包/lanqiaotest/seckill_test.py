import unittest

# 自动化测试        
# 如果不会设置Chrome驱动，请把chromedriver.exe复制到C盘根目录下，参考代码如下：
# service = Service("C:\\chromedriver.exe")

# 如果遇到无法启动chrome，控制台显示500的error
# 可以尝试取消沙盒模式，增加--no-sandbox参数来解决。参考代码如下：
# opt = Options()
# opt.add_argument('--no-sandbox')
# self.driver = webdriver.Chrome(chrome_options = opt, service=service)

class SeckillTest(unittest.TestCase):