# tests.py

import random
import time
try:
    import unittest2 as unittest
except ImportError:
    import unittest



def emptymesh():
  if 2 > 1:
    print ("run emptymesh")
    time.sleep (3)
    return True
  else:
    return False 

def 01sweep():
  if 2 > 1:
    print ("run emptymesh")
    time.sleep (5)
    return True
  else:
    return False



# call the testcases
class SimpleTest(unittest.TestCase):

    def test_emptymesh(self):
        self.failUnless(emptymesh())

    def test_01sweep(self):
        self.failUnless(01sweep())