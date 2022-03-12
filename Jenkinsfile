pipeline {
    agent any
    stages {
        stage("Docker Unit Test") {
            steps {
                sh "./run_tests.sh"
            }   
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