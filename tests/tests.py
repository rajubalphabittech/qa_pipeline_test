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
        print ("pass...start")
        cmd = "sudo cd /mnt/dev/mp_vision-build/deploy/ && ./vision_mesh_code.work /mnt/dev/mp_vision-build/deploy/ /mnt/dev/testResults/emptymesh/"
        process = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        process.wait()
        out, err = process.communicate()
        print ("Return code: ", process.returncode)
        print (out.rstrip(), err.rstrip())
        print ("pass...end")
      except:
        print ("Fail")
        return False

      return True




if __name__ == '__main__':
    unittest.main()