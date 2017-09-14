node {
    stage('Example') {
        try {
            sh 'ls -l'
        }
        catch (Exception e) {
            echo 'Something failed'
            throw e
        }
    }
}
