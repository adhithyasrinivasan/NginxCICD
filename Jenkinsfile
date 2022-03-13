node {
    checkout scm
    stage('Build Image') {
        def myEnv = docker.build 'nginxtest:2'
        myEnv.inside {
            sh 'nginx -v'
        }
    }
    /*stage('Run Container Tests') { //Commented this for now as these tests will not be able to run in jenkins DIND.
        def testImage = docker.build(
                "google-container-tests",
                "./tests/",
        )

        testImage.inside('-v tests:/tests') {
            sh "ls -al /tests"
            sh '/container-structure-test test -i nginxtest:2 -c ${WORKSPACE}/tests/test_config.yaml'
        }
    }*/
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
