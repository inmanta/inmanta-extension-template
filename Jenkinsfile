pipeline {
  agent any

  triggers {
    pollSCM '* * * * *'
    cron("H H(2-5) * * *")
  }

  options {
    disableConcurrentBuilds()
    checkoutToSubdirectory('inmanta-extension-template')
    skipDefaultCheckout()
  }

  stages {
    stage("Cleanup environment"){
      steps{
        sh '''
          rm -rf project env
          python3 -m venv ${WORKSPACE}/env
        '''
      }
    }
    stage("Setup extension project via cookiecutter"){
      steps{
        sh '''
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
          pip install -c ${WORKSPACE}/project/requirements.txt -U tox tox-venv setuptools pip
          make -C ${WORKSPACE}/project build-pytest-inmanta-extensions
        '''
      }
    }
    stage("Run tests"){
      steps{
        sh '''
          ${WORKSPACE}/env/bin/tox -e pep8,py36
        '''
      }
    }
  }
}