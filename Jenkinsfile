pipeline {
  agent {
    node {
      label 'master'
    }
  }
  stages {
    stage('Smoke Tests') {
      agent { label "master"}
        steps {
          sh "ls -l"
          writeFile file: 'testrun_id', text: '12345'
          stash includes: 'testrun_id', name: 'testrun'
        }
        post {
          always {
            echo "Posting from ALWAYS"
          }
          success {
            sh 'echo "run a scipt after SUCCESS"'
            script {
              // save this value for later...
              testrun_id = sh(returnStdout: true, script: 'echo "test666"').trim()
              smokeTestrun_id = readFile("testrun_id")

            }
          }
        }
      }

    stage('Regression Tests') {
      parallel {
        stage('Pro tests') {
          agent { label "master" }
            steps {
              echo 'Pro tests started'
              script {       
                // Test that fails...
                sh "ls -l"
                }
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
                sh "ls -l"
                // long ruinning test...
                sleep 10
                }
              post {
                success {
                  echo "Pro2 tests -- DONE"
                  }
                }
              }
          } // End parallel
        }
      }
  post {
    always {
      echo "Post at end of parallel..."
      sh 'echo "Damn you Jenkins!"'
      // Does unstash work here?
      unstash 'testrun'
      // Placeholder to run closeTestRun.py
      sh 'python3 --version'
      echo "${testrun_id}"
      echo "${smokeTestrun_id}"
      // Placeholder to run runTestRailreport.py
      sh 'python3 --version'
      }
    } // end of post
  options {timestamps()
  } 
}
 
