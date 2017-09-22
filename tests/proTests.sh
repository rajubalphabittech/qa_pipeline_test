#!/bin/bash 

# source the unit test for scripts functions
. jshutest.inc


# unit test functions


Emptymesh_FAIL_Test() {
	{ # try
		# process the model
		#cd /mnt/dev/mp_vision-build/deploy/ && ./vision_mesh_code.work /mnt/dev/mp_vision-build/deploy/ /mnt/dev/testResults/emptymesh/
		# test images
		cd /mnt/dev/qa/automation/jenkins/ && ./imageCompare.sh '/mnt/dev' 4 'pan/high' '72e2e8bdf87c45e29d023e7e18af1cc1_skybox1.jpg' '01sweep'
	} || { # catch
		return ${jshuFAIL}
	}
	return ${jshuPASS}	
}




##############################################################
# main
##############################################################
# initialize testsuite
jshuInit

# run unit tests on script
jshuRunTests

# result summary
jshuFinalize

echo Done.
echo
let tot=failed+errors
exit $tot

