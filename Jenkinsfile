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
    checkout scm
    stage('Build Image') {
        def myEnv = docker.build 'nginxtest:2'
        myEnv.inside {
            sh 'nginx -v'
        }
    }
    stage('Run Container Tests') {
        node ("gcrcontainer") {
            def testImage = docker.build(
                "google-container-tests",
                "./tests/Dockerfile",
            )

            testImage.inside('-v ./tests:/tmp') {
                sh '/container-structure-test test -i nginxtest:2'
            }
        }
    }
    stage('Deploy and Test Image') {
        docker.image('nginxtest:2').withRun('-p 8082:8082') { c ->
            docker.image('centos:7').inside("--link ${c.id}:nginx") {
                sh 'curl nginx:8082'
            }
            //sh 'netstat -napt | grep LIST'
            //sh 'ps -ef'
        }
    }
}
