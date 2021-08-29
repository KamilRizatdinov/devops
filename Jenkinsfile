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
                sh 'pk add --no-cache git'
                sh 'git clone https://github.com/KamilRizatdinov/devops.git'
                sh 'cd devops'
                sh 'pip install -r requirements.txt.development'
                sh 'cd python_app'
                sh 'pytest .'
            }
        }
    }
}
