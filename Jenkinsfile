pipeline {
    agent none
    stages {
      stage('Regression Tests') {
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
          script {
            sh 'echo "close the run..."'
              }
            }
          }
        } // End of stage
    }
}
 

