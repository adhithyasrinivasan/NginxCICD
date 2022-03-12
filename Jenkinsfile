pipeline {
    agent any
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'nginx -v'
                sh 'cat /usr/share/nginx/html/index.html'
                sh 'curl localhost:80'
            }
        }
    }
}