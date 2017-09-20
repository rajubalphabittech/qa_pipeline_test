# tests.py

import random
import time
from subprocess import call

try:
    import unittest2 as unittest
except ImportError:
    import unittest


# call the testcases
class ProTests(unittest.TestCase):

    def test_Pro10sweeps():
      try:
        call(["cd", "/mnt/dev/mp_vision-build/deploy/", "&&", "./vision_mesh_code.work", "/mnt/dev/mp_vision-build/deploy/", "/mnt/dev/testResults/emptymesh/"])
        return False
      except:
        return False




if __name__ == '__main__':
    unittest.main()