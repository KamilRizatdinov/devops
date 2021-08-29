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
                sh 'cd devops/python_app && pip install -r requirements.txt.development'
                sh 'cd devops/python_app && pytest .'
              }
            }
        }
    }
}
