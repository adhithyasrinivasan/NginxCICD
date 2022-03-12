pipeline {
    agent any
    stages {
        stage('Run') {
            agent { 
                    dockerfile true
                }
            steps {
                sh 'nginx -v'
                sh 'cat /usr/share/nginx/html/index.html'
            }
        }
    }
}