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
          sh '/bin/sh -xe ./proTests.sh'
          }
        }
      post {
        always {
          archiveArtifacts 'tests/results/*.xml'
          junit 'tests/results/*.xml'
          }
        }
      }

    } // End Stages
} // End pipeline
 

