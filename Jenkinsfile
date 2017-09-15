#!/usr/bin/env groovy

pipeline {
  agent { label 'master' }
  stages {
    stage('Build') {
      steps {
        dir(path: 'test/') {
          script {
            sh 'ls -l > list.log'
          }
        }
      archiveArtifacts 'list.log'
      }
    }
  }
}
