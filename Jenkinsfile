#!/usr/bin/env groovy

pipeline {
  agent { label 'master' }
  stages {
    stage('Build') {
      steps {
        dir(path: 'test/') {
          script {
            sh 'ls -l > list.log'
            sh 'ls foo'
          }
        }
      }
      post {
          always {
            sh "echo 'always'"
                  }
          failure {
            // test image fails
            archiveArtifacts 'list.log'
            slackSend channel: '#jenkins-qa', color: 'danger', message: "${currentBuild.displayName}\nPro empty mesh - FAILED"
              }
            }
          }
        }
      }
 

