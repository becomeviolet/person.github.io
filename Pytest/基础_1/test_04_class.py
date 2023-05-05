# 测试类形式
import pytest


class TestDemo(object): # 测试类名必须以 Test开头
    """测试示例类"""
    def test_method1(self):
        """测试方法1"""
        print('测试方法1')
    def test_method2(self):
        """测试方法2"""
        print('测试方法2')


if __name__ == '__main__':
    # pytest.main(['-s','文件名.py'])
    pytest.main(['-s', 'test_04_class.py'])