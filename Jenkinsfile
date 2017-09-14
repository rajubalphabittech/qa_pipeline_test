pipeline {
    stages {
        stage('Example') {
            script {
                try {
                    sh 'ls -l'
                } catch (Exception e) {
                    echo 'Something failed'
                    throw e
                }
            }
        }
    }
}
