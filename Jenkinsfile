pipeline {
  agent any
  stages {
    stage('Buid') {
      steps {
        sh 'ls foo'
      }
      post {
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