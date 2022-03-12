pipeline {
    agent any
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'curl localhost:80'
            }
        }
    }
}