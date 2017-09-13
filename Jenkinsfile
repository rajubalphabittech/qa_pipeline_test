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
        sh 'ls foo'
        slackSend channel: '#jenkins-qa', color: 'danger', message: 'Start...'
      }
    }
  }
}

