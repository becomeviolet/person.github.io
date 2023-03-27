from 蓝桥杯模拟赛源码.three_point_one_line import ThreePointOneLine

import unittest

class ThreePointOneLineTest(unittest.TestCase):

    def setUp(self) -> None:
        self.three_point_one_line = ThreePointOneLine()

    def test_is_one_line(self):
        self.assertFalse(self.three_point_one_line.is_one_line(1,2 ,1,2, 1,2))
        self.assertFalse(self.three_point_one_line.is_one_line(1,2, 1,2, 3,3))
        self.assertFalse(self.three_point_one_line.is_one_line(1,2, 3,3, 3,3))
        self.assertFalse(self.three_point_one_line.is_one_line(1,2, 2,3, 3,3))
        self.assertTrue(self.three_point_one_line.is_one_line(1,1, 1,2, 1,3))
        self.assertTrue(self.three_point_one_line.is_one_line(1,1, 2,1, 3,1))
        self.assertTrue(self.three_point_one_line.is_one_line(1,1, 2,2, 3,3))

if __name__ == '__main__':
    unittest.main()