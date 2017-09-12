pipeline {
  agent any
  stages {
    stage('Setup') {
      steps {
        sh 'ls -l'
      }
    }
    stage('Build') {
      steps {
        sh 'echo "test build"'
      }
    }
    stage('Slack msg') {
      steps {
        slackSend(message: 'Done!', channel: '#jenkins-qa', color: 'danger', teamDomain: 'matterport')
      }
    }
  }
}