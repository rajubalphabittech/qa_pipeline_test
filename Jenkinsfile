#!/usr/bin/env groovy

pipeline {
  agent { label 'master' }
  stages {
    stage('Build') {
      steps {
        dir(path: '/mnt/dev/') {
          script {
            sh 'ls -l > list.log'
          }
        }
        archiveArtifacts 'list.log'
      }
    }
  }
}
