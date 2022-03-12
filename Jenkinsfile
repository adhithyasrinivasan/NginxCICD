pipeline {
    stages {
        stage("Docker Unit Test") {
            sh run_tests.sh
        }
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
}