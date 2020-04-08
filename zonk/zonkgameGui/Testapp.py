from tkinter import *
from tkinter import messagebox
import unittest
from app import ZonkGame

class Testapp(unittest.TestCase):
    def setUp(self):
        self.zonk=ZonkGame() 
    def test(self):
        self.assertEqual(self.zonk.score([2,2,2,1,1,1]),1200)
        self.assertEqual(self.zonk.score([2,3,2,2,3,3]),500)
        self.assertEqual(self.zonk.score([5,5,3,2,3,3]),400)
        self.assertEqual(self.zonk.score([6,5,4,3,2,1]),1500)
        self.assertEqual(self.zonk.score([3,4,1,6,2,5]),1500)
        self.assertEqual(self.zonk.score([2,2,3,3,5,5]),750)
        self.assertEqual(self.zonk.score([1,1,1,1,1,1]),4000)
        self.assertEqual(self.zonk.score([2,2,2,2,2,2]),800)
        self.assertEqual(self.zonk.score([3,3,3,3,3,3]),1200)
        self.assertEqual(self.zonk.score([4,4,4,4,4,4]),1600)
        self.assertEqual(self.zonk.score([5,5,5,5,5,5]),2000)
        self.assertEqual(self.zonk.score([6,6,6,6,6,6]),2400)
        self.assertEqual(self.zonk.score([1,3,3,3,1,1]),1300)
        self.assertEqual(self.zonk.score([5,1,1,1,1,5]),2100)
        self.assertEqual(self.zonk.score([5,3,3,3,3,3]),950)
        self.assertEqual(self.zonk.score([4,4,4,4,4,5]),1250)
        self.assertEqual(self.zonk.score([1,1,2,2,3,3]),750)
        self.assertEqual(self.zonk.score([6,6,6,1,6,6]),1900)
        self.assertEqual(self.zonk.score([6,6,1,1,6,6]),1400)
        self.assertEqual(self.zonk.score([2,2,2,2,1,2]),700)
        self.assertEqual(self.zonk.score([3,3,3,1,5,5]),500)
if __name__=="__main__":
    unittest.main()
