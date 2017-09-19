# tests.py

import random
import time
try:
    import unittest2 as unittest
except ImportError:
    import unittest


# test cases steps
def Proemptymesh():
  if 2 > 1:
    print ("run Pro emptymesh")
    time.sleep (3)
    return True
  else:
    return False 

def Pro01sweep():
  return False

def Pro10sweeps():
  if 2 > 1:
    print ("run Pro 10 sweeps")
    time.sleep (5)
    return True
  else:
    return False 

def Pro3014NE137th():
  if 2 > 1:
    print ("run 3014 NE 137th")
    time.sleep (6)
    return True
  else:
    return False



# call the testcases
class ProTests(unittest.TestCase):

    def test_Proemptymesh(self):
        self.failUnless(Proemptymesh())

    def test_Pro01sweep(self):
        self.failUnless(Pro01sweep())

    def test_Pro10sweeps(self):
        self.failUnless(Pro10sweeps())

    def test_Pro3014NE137th(self):
        self.failUnless(Pro3014NE137th())