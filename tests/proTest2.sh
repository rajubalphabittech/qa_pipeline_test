#/bin/sh

#### Include the library
. `dirname $0`/sh2ju.sh


# Test cases
proEmptymesh() {
   # process the model
   { # try
       cd /mnt/dev/qa/automation/jenkins/ && ./imageCompare.sh '/mnt/dev' .1 'pan/high' '72e2e8bdf87c45e29d023e7e18af1cc1_skybox1.jpg' '01sweep'
   } || { # catch
       return 1 
   }
   return 0
}

juLog  -name=proEmptymesh             proEmptymesh

