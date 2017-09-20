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
        print ("pass...start")
        process = subprocess.check_output(['cd', '/mnt/dev/mp_vision-build/deploy/', '&&', './vision_mesh_code.work', '/mnt/dev/mp_vision-build/deploy/', '/mnt/dev/testResults/emptymesh/'], shell=True)
        #process = subprocess.Popen(['cd', '/mnt/dev/mp_vision-build/deploy/', '&&', './vision_mesh_code.work', '/mnt/dev/mp_vision-build/deploy/', '/mnt/dev/testResults/emptymesh/'], stdout=subprocess.PIPE)
        print ("pass...end")
      except:
        print ("Fail")
        return False

      return True




if __name__ == '__main__':
    unittest.main()