pipeline {
  agent any
  stages {
    stage('Buid') {
      steps {
        sh 'ls -l /mnt/dev > list.log
        sh 'ls foo'
      }
      post {
        always {
          archiveArtifacts 'list.log'
        }
        success {
          echo 'I succeeded!'
        }
        failure {
          echo 'I failed :('
        }
        
      }
    }
    stage('test') {
      steps {
        sh 'ls'
      }
    }
  }
}
