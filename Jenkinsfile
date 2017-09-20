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
          sh 'nose2 --plugin nose2.plugins.junitxml --junit-xml tests'
          }
        }
      post {
        always {
          archiveArtifacts 'tests/*.xml'
          junit 'tests/*.xml'
          }
        }
      }

    } // End Stages
} // End pipeline
 

