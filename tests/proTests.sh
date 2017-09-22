#!/usr/bin/env bats

@test "Pro empty mesh" {
        # test image
        cd /mnt/dev/qa/automation/jenkins/ && ./imageCompare.sh '/mnt/dev' 4 'pan/high' '72e2e8bdf87c45e29d023e7e18af1cc1_skybox1.jpg' '01sweep'
        [ $status = 0 ]
}
