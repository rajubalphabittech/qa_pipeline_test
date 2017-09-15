pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        dir(path: '~/')
        script {
          sh -l > list.log
        }
        
        archiveArtifacts 'list.log'
      }
    }
  }
}