#!/usr/bin/env groovy

pipeline {
  agent { label 'master' }
  stages {
    stage('Build') {
      dir(path: '/mnt/dev/') {
          script {
            sh 'ls -l > list.log'
          }
        }
      archiveArtifacts 'list.log'
      }
    }
  }
