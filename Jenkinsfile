pipeline {
    agent none
    stages {
      stage('Regression Tests') {
        steps {
          echo "Can I do something here....?"
        }
        
        parallel {
          stage('Pro tests') {
            agent { label "master" }
              steps {
                    echo 'Pro tests started'
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
            }
          }
        } // End of stage
    }
}
 

