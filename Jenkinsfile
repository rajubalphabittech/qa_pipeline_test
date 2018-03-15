pipeline {
    agent none
    stages {
      stage('Regression Tests') {
        parallel {
          stage('Pro tests') {
            agent { label "master" }
              steps {
                    echo 'Pro tests'
                    }
              post {
                success {
                  echo "Pro tests DONE"
                    }
                  }
              }

            stage('Pro2 Tests') {
              agent { label "master" }
                steps {
                      echo 'Pro2 tests'
                      }
                post {
                   success {
                      echo "Pro tests DONE"
                      }
                    }
                }
            
            post {
              always {
                echo 'Close test run for Regression Tests'
              }
            }
          } // End parallel
        }
    }
}
 

