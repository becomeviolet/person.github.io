"""
特殊方法：函数级别和类级别同时使用
"""
import pytest


class TestDemo(object):
    """示例测试类"""
    def setup_class(self):
        print('类级别 ->> 开始')

    def tear_class(self):
        print('类级别 ->> 结束')

    def setup(self):
        print('函数级别 -> 开始')

    def teardown(self):
        print('函数级别 -> 结束')

    def test_method1(self):
        """测试方法1"""
        print('测试方法1')

    def test_method2(self):
        """测试方法2"""
        print('测试方法2')


if __name__ == '__main__':
    pytest.main(['-s','test_07_SF_fuc_and_class.py'])