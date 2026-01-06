pipeline {
  agent any

  triggers {
    cron("H H(2-5) * * *")
  }

  environment {
    PIP_INDEX_URL='https://artifacts.internal.inmanta.com/inmanta/dev'
  }

  options {
    disableConcurrentBuilds()
    checkoutToSubdirectory('inmanta-extension-template')
    skipDefaultCheckout()
  }

  stages {
    stage("clear workspace and checkout source code"){
      steps{
        deleteDir()
        dir('inmanta-extension-template') {
          checkout scm
        }
      }
    }
    stage("Setup extension project via cookiecutter"){
      steps{
        sh '''
          python3 -m venv ${WORKSPACE}/env
          source ${WORKSPACE}/env/bin/activate
          pip install -c ${WORKSPACE}/inmanta-extension-template/requirements.txt cookiecutter
          # This creates an Inmanta extension project called 'project'
          cookiecutter --no-input ${WORKSPACE}/inmanta-extension-template
        '''
      }
    }
    stage("Install test dependencies"){
      steps{
        sh '''
          source ${WORKSPACE}/env/bin/activate
          pip install -r ${WORKSPACE}/project/requirements.txt
        '''
      }
    }
    stage("Run tests"){
      steps{
        dir('project') {
          sh '''
            ${WORKSPACE}/env/bin/flake8 src tests
            ${WORKSPACE}/env/bin/pytest tests
          '''
        }
      }
    }
  }
  post{
    cleanup{
      deleteDir()
    }
  }
}
