#!/bin/bash 

# source the unit test for scripts functions
. jshutest.inc


# helper function
# remove host and date lines from buildnumber.txt file
stripHostDate() {
	source="$1"
	dest="$2"
	grep -v '^BuildHost:' $source | grep -v '^Date' >$dest
}

# In this one, we don't source the other script because
# we're not going to test pieces of it. We're just going
# to run the script and evaluate what it does.
##############################################################
# unit test functions
proEmptymesh_Test() {
	# process the model
	ls -l > text.log
    a=10
	b=20
	if [ $a == $b ]; then
		return ${jshuFAIL}
	fi
		echo "PASS"
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