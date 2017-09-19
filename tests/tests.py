# tests.py

import random
import time
try:
    import unittest2 as unittest
except ImportError:
    import unittest



def Proemptymesh():
  if 2 > 1:
    print ("run emptymesh")
    time.sleep (3)
    return True
  else:
    return False 

def Pro01sweep():
  if 2 > 1:
    print ("run emptymesh")
    time.sleep (5)
    return True
  else:
    return False



# call the testcases
class SimpleTest(unittest.TestCase):

    def test_emptymesh(self):
        self.failUnless(Proemptymesh())

    def test_01sweep(self):
        self.failUnless(Pro01sweep())