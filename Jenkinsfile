pipeline {
  agent any
  stages {
    stage('Buid') {
        steps {
          script {
             sh 'ls -l /mnt/dev > list.log'
             sh 'ls foo'
             }
          }
         post {
           success {
              echo 'I succeeded!'
               }
           failure {
              echo 'I failed :('
              slackSend channel: '#jenkins-qa', color: 'danger', message: 'Testing post fail process'
              archiveArtifacts 'list.log'
               }
            }
      }

    stage('test') {
      steps {
        sh 'ls'
            }
        }
    }
}
