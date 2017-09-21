# tests.py

import random
import time
import subprocess
from subprocess import Popen, PIPE

try:
    import unittest2 as unittest
except ImportError:
    import unittest




# call the testcases
class ProTests(unittest.TestCase):

    def test_Pro10sweeps(self):
      try:
        print ("process image")
        cmd = "cd /mnt/dev/mp_vision-build/deploy/ && ./vision_mesh_code.work /mnt/dev/mp_vision-build/deploy/ /mnt/dev/testResults/emptymesh/"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()
        output = process.stderr.read()
        print (output)
        print ("test image")
        cmd2 = "cd /mnt/dev/qa/automation/jenkins/ && ./imageCompare.sh '/mnt/dev' .1 'pan/high' '72e2e8bdf87c45e29d023e7e18af1cc1_skybox1.jpg' '01sweep'"
        process = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
        process.wait()
        output = process.stderr.read()
        print (output)
      except:
        return False

      return True




if __name__ == '__main__':
    unittest.main()