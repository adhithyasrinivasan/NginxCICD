// pipeline {
//     agent any
//     stages {
//         stage('Run') {
//             agent {
//                     dockerfile true
//                 }
//             steps {
//                 sh 'nginx -v'
//                 sh 'cat /usr/share/nginx/html/index.html'
//             }
//         }
//     }
// }

node {
    stage('Build Image') {
        def myEnv = docker.build 'nginxtest:1'
        myEnv.inside {
            sh 'nginx -v'
        }
    }
    stage('Deploy and Test Image') {
        docker.image('nginxtest:1').withRun('-p 8082:8082') { c ->
            docker.image('centos:7').inside("--link ${c.id}:nginx") {
                sh 'curl nginx:8082'
            }
            //sh 'netstat -napt | grep LIST'
            //sh 'ps -ef'
        }
    }
}
