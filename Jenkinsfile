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
                sh 'apk add --no-cache git'
                sh 'rm -rf devops'
                sh 'git clone https://github.com/KamilRizatdinov/devops.git'
                dir('devops/python_app') {
                  sh 'ls'
                }
            }
        }
    }
}
