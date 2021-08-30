pipeline {
  agent {
    docker {
      image 'python:3.7-alpine'
      args '-u 0 -v /var/run/docker.sock:/var/run/docker.sock'
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
        sh 'apk add gcc musl-dev docker'
      }
    }

    stage('Install python dependencies') {
      steps {
        withPythonEnv('python') {
          sh 'ls'
          sh 'pip install -r $workdir/requirements.txt.development'
        }
      }
    }

    stage('Run python tests') {
      steps {
        withPythonEnv('python') {
          sh 'cd $workdir && pytest .'
        }
      }
    }

    stage('Check with black') {
      steps {
        withPythonEnv('python') {
          sh 'cd $workdir && black --check --verbose .'
        }
      }
    }

    stage('Building image') {
      steps{
        script {
          docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
  }
}
