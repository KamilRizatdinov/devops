pipeline {
    agent {
      docker {
        image 'python:3.7-alpine'
        args '-u 0'
      }
    }

    stages {
        stage('test') {
            steps {
              dir(path: env.BUILD_ID) {
                sh 'apk add --no-cache git'
                sh 'git clone https://github.com/KamilRizatdinov/devops.git'
                dir('devops/python_app') {
                  sh 'ls'
                }
              }
            }
        }
    }
}
