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
      try {
        steps {
          sh 'ls foo' 
        }
      }
      catch (exc) {
        slackSend channel: '#jenkins-qa', color: 'danger', message: 'Start...'
      }
    }
  }
}

