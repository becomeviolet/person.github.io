'''
从被测代码来看，是可以与基本路径覆盖相同
'''

from 蓝桥杯模拟赛源码.three_point_one_line import ThreePointOneLine

import unittest

class ThreePointOneLineTest(unittest.TestCase):

    def setUp(self) -> None:
        self.three_point_one_line = ThreePointOneLine()

    def test_is_one_line(self):
        self.assertFalse(self.three_point_one_line.is_one_line(1,2 ,1,2, 1,2))#三点相同
        self.assertFalse(self.three_point_one_line.is_one_line(1,2, 1,2, 3,3))#前两点相同
        self.assertFalse(self.three_point_one_line.is_one_line(1,2, 3,3, 3,3))#后两点相同
        self.assertFalse(self.three_point_one_line.is_one_line(1,2, 2,3, 3,3))#正常情况非同线
        self.assertTrue(self.three_point_one_line.is_one_line(1,1, 1,2, 1,3))#特殊情况3点横坐标相同
        self.assertTrue(self.three_point_one_line.is_one_line(1,1, 2,1, 3,1))#特殊情况3点纵坐标相同
        self.assertTrue(self.three_point_one_line.is_one_line(1,1, 2,2, 3,3))#正常情况共线

if __name__ == '__main__':
    unittest.main()
