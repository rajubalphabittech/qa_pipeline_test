#!/usr/bin/env groovy

pipeline {
  agent { label 'master' }
  stages {


  // space is nice


    stage('Build') {
      steps {
        dir(path: 'tests/') {
          script {
            sh 'ls -l > list.log'
            sh 'ls'
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
            slackSend channel: '#jenkins-qa', color: 'danger', message: "${currentBuild.displayName}\nreport - FAILED"
              }
            }
          }

    stage ('Test') {
      steps {
        dir(path: 'tests/') {
          sh 'pwd'
          sh 'nose2 --plugin nose2.plugins.junitxml --junit-xml tests'
          archiveArtifacts '*.xml'
          }
        }
      }
    post {
      always {
        junit '*.xml'
      }
    }

    } // End Stage
} // End pipeline
 

