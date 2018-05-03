pipeline {
  agent {
    node {
      label 'master'
    }
  }
  triggers {
    pollSCM('* * * * *') //runs this pipeline on every commit
    cron('30 14 * * *') //run at 14:30:00 
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
          when {//runs only when the expression evaluates to true
                expression {//will return true when the build runs via cron trigger (also when there is a commit at night between 14:00 and 14:59)
                    return Calendar.instance.get(Calendar.HOUR_OF_DAY) in 14
                }
            }
          agent { label "master"}
            steps {
              echo 'SmokeTest 2'
              sleep 2
              sh "ls -l"
            }
          }
        }
      }

    stage('Regression Tests') {
      parallel {
        stage('Regression 1') {
          agent { label "master" }
            steps {
              echo 'Regression 1'
            }
          }
        stage('Regression 2') {
          agent { label "master" }
            steps {
              echo 'Regression 2'
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
 
