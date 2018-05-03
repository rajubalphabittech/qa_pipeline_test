pipeline {
  agent {
    node {
      label 'master'
    }
  }
  stages {
    stage('Smoke Tests') {
      parallel {
        stage('SmokeTest 1') {
          agent { label "master"}
            steps {
              echo 'SmokeTest 1'
            }
          }
        stage('SmokeTest 2') {
          agent { label "master"}
            steps {
              echo 'SmokeTest 2'
              sleep 2
              sh "ls -5"
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
            }
          }
        stage('Pro2 Tests') {
          agent { label "master" }
            steps {
              echo 'Pro2 tests started'
              sh "ls -l"
              // long ruinning test...
              sleep 2
              }
            }
          } // End parallel
        }
      }
  options {timestamps()
  } 
}
 
