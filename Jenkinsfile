pipeline {
    agent none
    stages {
      stage('Regression Tests') {
        parallel {
          stage('Pro tests') {
            agent { label "master" }
              steps {
                    echo 'Pro tests started'
                    testrun_id = '1234'
                    writeFile file: 'automation/jenkins/testrun_id', text: "${testrun_id}"
                    }
              post {
                success {
                  echo "Pro tests -- DONE"
                    }
                  }
              }

            stage('Pro2 Tests') {
              agent { label "master" }
                steps {
                      echo 'Pro2 tests started'
                      }
                post {
                   success {
                      echo "Pro2 tests -- DONE"
                      }
                    }
                }
            } // End parallel
      post {
        always {
          echo 'Close test run for Regression Tests'
          new_testrun_id = readFile("automation/jenkins/testrun_id")
            }
          }
        } // End of stage
    }
}
 

