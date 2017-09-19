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
          sh 'sudo ./proTests.sh'
          archiveArtifacts '*.xml'
          }
        } 
      }   

    } // End Stages

  post {
      always {
        archiveArtifacts 'results/*.xml'
        junit 'results/*.xml'
      }
    }
} // End pipeline
 

