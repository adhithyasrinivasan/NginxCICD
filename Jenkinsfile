pipeline {
    agent any
    stages {
        stage('Test') {
            agent { 
                    dockerfile {
                    args '-it --entrypoint=/bin/bash' }
                }
            steps {
                sh 'nginx -v'
                sh 'cat /usr/share/nginx/html/index.html'
                sh 'curl localhost:80'
            }
        }
    }
}