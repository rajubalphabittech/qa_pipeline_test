# tests.py

import random
import time
import subprocess

try:
    import unittest2 as unittest
except ImportError:
    import unittest





# call the testcases
class ProTests(unittest.TestCase):

    def test_Pro10sweeps(self):
      try:
        process = subprocess.Popen(['cd', '/mnt/dev/mp_vision-build/deploy/', '&&', './vision_mesh_code.work', '/mnt/dev/mp_vision-build/deploy/', '/mnt/dev/testResults/emptymesh/'], stderr=subprocess.PIPE)
        process.wait()
        return self.failUnless(True)
      except:
        print ("Fail")
        return self.failUnless(False)




if __name__ == '__main__':
    unittest.main()