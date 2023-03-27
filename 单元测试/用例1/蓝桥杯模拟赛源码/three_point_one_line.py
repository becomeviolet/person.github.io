# 题目:
#     按照从低点到高点的顺序依次输入平面三个坐标点, 利用斜率判断三个坐标点是否在一条直线上, 不允许有重合点.
# 要求:
#     请设计足够的测试用例，运行所测程序，要覆盖程序中所有可能的执行路径。
#     语言要求java或者python, 只能选一种, 两种语言都用的话, 会以java语言判分
#     包名： 定义的测试类需要放在com.lanqiao.test包中。
#     类名： 定义测试类，类名是由被测试类名Test构成, 文件名以_test结尾。例如：file_name_test。
#     方法名： 测试方法的方法名定义方式, test_测试方法。
#     返回值： 不需要处理任何返回值。
#     参数列表：方法无需传递参数。
# 按照从低点到高点的顺序依次输入平面三个坐标点, 利用斜率判断三个坐标点是否在一条直线上, 不允许有重合点.
# 要求编写逻辑清晰易读易懂
# float x1
# float y1
# float x2
# float y2
# float x3
# float y3
# return True 在一条直线上, False 不在一条直线上



class ThreePointOneLine:

    def is_one_line(self, x1, y1, x2, y2, x3, y3):
        #3点相同
        if x1 == x2 and x2 == x3 and y1 == y2 and y2 == y3:
            return False
        #2点相同1
        if x1 == x2 and y1 == y2 and x1 != x3 and y1 != y3:
            return False
        #2点相同情况2
        if x2 == x3 and y2 == y3 and x1 != x3 and y1 != y3:
            return False
        #3点横坐标相同，纵坐标不同
        if x1 == x2 and x2 == x3:
            if y1 != y2 and y2 != y3:
                return True
        #3点纵坐标相同，横坐标不同
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

