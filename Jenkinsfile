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
                      echo 'failing test...'
                      sh "ls -2"
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
            echo "Post at end of parallel..."
            node('master') {
              steps{
                sh 'echo "run something..."'
              }
            }
          }
          }
        }
      }
      stage ('Close test run') {
        steps {
          echo 'echo "Close the regression test run..."'
        }
      }   
    } // End of stage
  }
 

