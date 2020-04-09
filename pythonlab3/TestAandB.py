from AandB import AandB
import unittest

class TestAandB(unittest.TestCase):
    def setUp(self):
        self.test1=AandB(10,15)
        self.test2=AandB(0,0)
        self.test3=AandB(5,6)
        self.test4=AandB(25,30)
        self.test5=AandB(19,20)
        self.test6=AandB(40,41)
    def test1(self):
        self.assertEqual(self.test1.numbers(),[10,11,12,13,14,15])
    def test2(self):
        self.assertEqual(self.test2.numbers(),[0])
    def test3(self):
        self.assertEqual(self.test3.numbers(),[5,6])
    def test4(self):
        self.assertEqual(self.test4.numbers(),[25,26,27,28,29,30])
    def test5(self):
        self.assertEqual(self.test5.numbers(),[19,20])
    def test6(self):
        self.assertEqual(self.test6.numbers(),[40,41])

if __name__=="__main__":
    unittest.main()
