#!/bin/bash 

# source the unit test for scripts functions
. jshutest.inc


# unit test functions
myWorkSpace='/mnt/dev'


proEmptymesh_Test() {
	{ # try
		# process the model
		sh 'cd $myWorkSpace/mp_vision-build/deploy/ && ./vision_mesh_code.work $myWorkSpace/mp_vision-build/deploy/ $myWorkSpace/testResults/emptymesh/'
		# test images
		echo "test images..."
	} || { # catch
		return ${jshuFAIL}
	}
	return ${jshuPASS}	
}

pro2Emptymesh_Test() {
	# process the model
	{ # try
		echo "PASS"

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