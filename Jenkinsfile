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
      node ("master") {
        script {
          // Generate report...
          regression_report = readFile("automation/jenkins/testrun_id")
          echo 'Post report...'
          echo "${regression_report}"
          }
        }
      }
    } // end of post
  options {timestamps()
  } 
}
 
