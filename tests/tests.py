# tests.py

import random
import time
from subprocess import call

try:
    import unittest2 as unittest
except ImportError:
    import unittest


# test cases steps
def proEmptymesh():
  try:
    call(["cd", "/mnt/dev/mp_vision-build/deploy/", "&&", "./vision_mesh_code.work", "/mnt/dev/mp_vision-build/deploy/", "/mnt/dev/testResults/emptymesh/"])
    return True
  except OSError:
    return False



# call the testcases
class ProTests(unittest.TestCase):

    def test_Pro10sweeps(self):
        self.failUnless(proEmptymesh())