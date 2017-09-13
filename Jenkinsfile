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
        sh 'ls -ggdfh'
        slackSend(message: 'Fail?', channel: '#jenkins-qa', failOnError: true, color: 'danger')
      }
    }
  }
}