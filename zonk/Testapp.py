from tkinter import *
from tkinter import messagebox
import unittest
from app import ZonkGame

class Testapp(unittest.TestCase):
    def setUp(self):
        self.zonk=ZonkGame() 
    def test(self):
        self.assertEqual(self.zonk.score([2,2,2,1,1,1]),1200)
    def test1(self):
        self.assertEqual(self.zonk.score([2,3,2,2,3,3]),500)
    def test2(self):
        self.assertEqual(self.zonk.score([5,5,3,2,3,3]),400)
    def test3(self):
        self.assertEqual(self.zonk.score([6,5,4,3,2,1]),1500)
    def test4(self):
        self.assertEqual(self.zonk.score([3,4,1,6,2,5]),1500)
    def test5(self):
        self.assertEqual(self.zonk.score([2,2,3,3,5,5]),750)
    def test6(self):
        self.assertEqual(self.zonk.score([1,1,1,1,1,1]),4000)
    def test7(self):
        self.assertEqual(self.zonk.score([2,2,2,2,2,2]),800)
    def test8(self):
        self.assertEqual(self.zonk.score([3,3,3,3,3,3]),1200)
    def test9(self):
        self.assertEqual(self.zonk.score([4,4,4,4,4,4]),1600)
    def test10(self):
        self.assertEqual(self.zonk.score([5,5,5,5,5,5]),2000)
    def test11(self):
        self.assertEqual(self.zonk.score([6,6,6,6,6,6]),2400)
    def test12(self):
        self.assertEqual(self.zonk.score([1,3,3,3,1,1]),1300)
    def test13(self):
        self.assertEqual(self.zonk.score([5,1,1,1,1,5]),2100)
    def test14(self):
        self.assertEqual(self.zonk.score([5,3,3,3,3,3]),950)
    def test15(self):
        self.assertEqual(self.zonk.score([4,4,4,4,4,5]),1250)
    def test16(self):
        self.assertEqual(self.zonk.score([1,1,2,2,3,3]),750)
    def test17(self):
        self.assertEqual(self.zonk.score([6,6,6,1,6,6]),1900)
    def test18(self):
        self.assertEqual(self.zonk.score([6,6,1,1,6,6]),1400)
    def test19(self):
        self.assertEqual(self.zonk.score([2,2,2,2,1,2]),700)
    def test20(self):
        self.assertEqual(self.zonk.score([3,3,3,1,5,5]),500)
    def test21(self):
        self.assertEqual(self.zonk.score([1,2,3,4,5,6]),1500)
if __name__=="__main__":
    unittest.main()
