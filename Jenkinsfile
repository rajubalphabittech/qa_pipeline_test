pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        dir(path: '/mnt/dev/')
        script {
          sh -l > list.log
        }
        
        archiveArtifacts 'list.log'
      }
    }
  }
}