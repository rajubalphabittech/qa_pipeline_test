
pipeline {
    agent any
    stages {
        stage('Buid') {
            steps {
                sh 'ls'
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
         stage('Buid') {
            steps {
                sh 'ls'
            }
        }
    }
}
