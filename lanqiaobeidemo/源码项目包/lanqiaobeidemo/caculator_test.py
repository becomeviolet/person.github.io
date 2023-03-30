import unittest
from com.lanqiao.caculator import Caculator

# 单元测试

class CaculatorTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("test start------")
        
    def test_add(self):
        self.assertEqual(5,Caculator.add(self,3, 2))
        print("add")

    def test_substract(self):
        self.assertEqual(1,Caculator.substract(self,3,2))
        print("sub")

    def test_multi(self):
        self.assertEqual(6,Caculator.multi(self,3,2))
        print("multi")

    def test_divide(self):
        self.assertEqual(3,Caculator.divide(self,6,2))
        print("did")
        

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CaculatorTest("test_add"))
    suite.addTest(CaculatorTest("test_substract"))
    suite.addTest(CaculatorTest("test_divide"))
    suite.addTest(CaculatorTest("test_multi"))
    unittest.TextTestRunner().run(suite)
