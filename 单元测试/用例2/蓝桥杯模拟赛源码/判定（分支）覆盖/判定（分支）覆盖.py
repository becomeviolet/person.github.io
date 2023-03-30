'''
使得程序中每一个判断的取真和取假至少经历一次
9用例？
'''
import unittest
class ThreePointOneLine:

    def is_one_line(self, x1, y1, x2, y2, x3, y3):
        #3点相同 特殊情况1
        if x1 == x2 and x2 == x3 and y1 == y2 and y2 == y3:
            return False
        #1点与2点相同且一点与三点不同 特殊情况2
        if x1 == x2 and y1 == y2 and x1 != x3 and y1 != y3:
            return False
        #2点与3点相同且一点与三点不同 特殊情况3
        if x2 == x3 and y2 == y3 and x1 != x3 and y1 != y3:
            return False
        #3点横坐标相同且三点纵坐标不同  特殊情况4
        if x1 == x2 and x2 == x3:
            if y1 != y2 and y2 != y3:
                return True
        #3点纵坐标相同且横坐标不同  特殊情况5
        if y1 == y2 and y2 == y3:
            if x1 != x2 and x2 != x3:
                return True
        #前两点斜率
        slope1 = (y2 - y1) / (x2 - x1)
        #后两点斜率
        slope2 = (y3 - y2) / (x3 - x2)
        #比较
        if slope1 == slope2:
            return True
        return False

class ThreePointOneLineTest(unittest.TestCase):

    def setUp(self) -> None:
        self.three_point_one_line = ThreePointOneLine()

    def test_is_one_line(self):
        # 用例2 第一个分支全真覆盖 3点相同
        self.assertFalse(self.three_point_one_line.is_one_line(1,2, 1,2, 1,2))
        # 用例2 第二个分支全真覆盖 前2点相同  第一个分支真、假、真、假
        self.assertFalse(self.three_point_one_line.is_one_line(1, 2, 1, 2, 3, 3))
        # 用例3 第三个分支全真覆盖 后两点相同  第一个分支假、真、假、真 第一个判定全覆盖 第二个判定 假、假、真、真
        self.assertFalse(self.three_point_one_line.is_one_line(1, 2, 3, 3, 3, 3))
        # 用例4 第四个分支全真覆盖 3点横坐标相同，纵坐标不同     第二个判定 真、假、假、真 第三个判定：真、假、假、真
        self.assertTrue(self.three_point_one_line.is_one_line(1, 1, 1, 2, 1, 3))
        # 用例5 第5个分支全真覆盖  3点纵坐标相同，横坐标不同    第二个判定 假、真、真、假  第三个判定：假、真、真、假 第四个判定：
        self.assertTrue(self.three_point_one_line.is_one_line(1, 1, 2, 1, 3, 1))
        # 用例6 第6个分支真覆盖 正常情况3点共线
        self.assertTrue(self.three_point_one_line.is_one_line(1, 1, 2, 2, 3, 3))

if __name__ == '__main__':
    unittest.main()
