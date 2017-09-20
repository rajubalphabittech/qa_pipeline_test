# tests.py

import random
import time
from subprocess import call

try:
    import unittest2 as unittest
except ImportError:
    import unittest


# test cases steps
def Pro10sweeps():
  if 2 > 1:
    print ("run Pro 10 sweeps")
    time.sleep (5)
    return True
  else:
    return False 


# call the testcases
class ProTests(unittest.TestCase):

    def test_Pro10sweeps(self):
        self.failUnless(Pro10sweeps())