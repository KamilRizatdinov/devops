pipeline {
    agent { docker { image 'python:3.7-alpine' } }
    stages {
        stage('first') {
            steps {
                sh 'python --version'
            }
        }
    }
}
