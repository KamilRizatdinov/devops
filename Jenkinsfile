pipeline {
  agent {
    docker {
      image 'python:3.7-alpine'
      args '-u 0'
    }
  }

  environment {
    registry = 'rizatdinov/python_app'
    workdir = 'python_app'
  }

  stages {
    stage('Checkout git repository') {
      steps {
        checkout scm
      }
    }

    stage('Install alpine dependencies') {
      steps {
        sh 'ls'
        sh 'apk add gcc docker'
      }
    }

    stage('Install python dependencies') {
      steps {
        withPythonEnv('python') {
          sh 'pip install -r $workdir/requirements.development.txt'
        }
      }
    }

    stage('Run python tests') {
      steps {
        withPythonEnv('python') {
          sh 'pytest $workdir/.'
        }
      }
    }
  }
}
