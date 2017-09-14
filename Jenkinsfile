pipeline {
    stages {
        stage('Example') {
            step {
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
}
