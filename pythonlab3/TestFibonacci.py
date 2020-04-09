from fibonacci import fibonacci
import unittest

class Testfibonacci(unittest.TestCase):
    def setUp(self):
        self.test1=fibonacci(40)
        self.test2=fibonacci(50)
        self.test3=fibonacci(56)
        self.test4=fibonacci(70)
        self.test5=fibonacci(80)
        self.test6=fibonacci(90)
        self.test7=fibonacci(0)
    def test1(self):
        self.assertEqual(self.test1.fibo(),102334155)
    def test2(self):
        self.assertEqual(self.test2.fibo(),12586269025)
    def test3(self):
        self.assertEqual(self.test3.fibo(),225851433717)
    def test4(self):
        self.assertEqual(self.test4.fibo(),190392490709135)
    def test5(self):
        self.assertEqual(self.test5.fibo(),23416728348467685)
    def test6(self):
        self.assertEqual(self.test6.fibo(),2880067194370816120)
    def test7(self):
        self.assertEqual(self.test7.fibo(),0)
if __name__=="__main__":
    unittest.main()
