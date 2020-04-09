from findmax import array
import unittest

class Testfindmax(unittest.TestCase):
    def setUp(self):
        self.test1=array([30,40,23,60,2])
        self.test2=array([23,100,33,4,2,30,45,23])
        self.test3=array([0])
        self.test4=array([1,3,4,5,6,7,1,2,7,3])
        self.test5=array([3,2,1,3])
        self.test6=array([1])
        self.test7=array([-1])
    def test1(self):
        self.assertEqual(self.test1.prepare(),60)
    def test2(self):
        self.assertEqual(self.test2.prepare(),100)
    def test3(self):
        self.assertEqual(self.test3.prepare(),0)
    def test4(self):
        self.assertEqual(self.test4.prepare(),7)
    def test5(self):
        self.assertEqual(self.test5.prepare(),3)
    def test6(self):
        self.assertEqual(self.test6.prepare(),1)
    def test7(self):
        self.assertEqual(self.test7.prepare(),-1)
if __name__=="__main__":
    unittest.main()
