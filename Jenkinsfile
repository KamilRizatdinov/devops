pipeline {
    environment {
      registry = 'rizatdinov/python_app'
    }

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
                sh 'apk add git build-base'
                sh 'git clone https://github.com/KamilRizatdinov/devops.git'
                sh 'cd devops/python_app && pip install -r requirements.txt.development'
                sh 'cd devops/python_app && pytest .'
              }
            }
        }
        stage('build') {
          steps {
            dir(path: env.BUILD_ID) {
              sh 'apk add docker openrc'
              sh 'rc-update add docker boot'
              script {
                sh 'cd devops/python_app && docker build -t $registry:$env.BUILD_ID .'
              }
            }
          }
        }
    }
}
