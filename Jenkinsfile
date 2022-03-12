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
  def myEnv = docker.build 'nginxtest:1'
  myEnv.inside {
    sh 'nginx -v'
    sh 'curl localhost:80'
  }
}