'''
基础_1：流图区域的数量对应环型复杂性
2：给定流图G的圈复杂度V(G)
公式一：边-判定节点+2
公式二：判定节点+基础_1
有效判定节点？判定节点：6
特殊情况1用例，正常情况2用例?
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