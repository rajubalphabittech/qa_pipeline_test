pipeline {
  agent {
    node {
      label 'master'
    }
  }
  stages {
    stage('Regression Tests') {
      parallel {
        stage('Pro tests') {
          agent { label "master" }
            steps {
              echo 'Pro tests started'
              script {
                testrun_id = 12345
                writeFile file: 'automation/jenkins/testrun_id', text: "${testrun_id}"
                // Test that fails...
                sh "ls -4"
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
      // Placeholder to run closeTestRun.py
      //sh 'python3 --version'
      result = sh(returnStdout: true, script: 'python3 -- version').trim()
      echo "${result}"
      // Placeholder to run runTestRailreport.py
      sh 'python3 --version'
      }
    } // end of post
  options {timestamps()
  } 
}
 
