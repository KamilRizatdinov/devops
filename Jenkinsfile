pipeline {
    agent { docker { image 'python:3.7-alpine' } }
    stages {
        stage('test') {
            steps {
                sh 'git pull https://github.com/KamilRizatdinov/devops.git'
                sh 'cd devops'
                sh 'pip install -r requirements.txt.development'
                sh 'cd python_app'
                sh 'pytest .'
            }
        }
    }
}
