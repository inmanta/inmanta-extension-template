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
        withCredentials([string(credentialsId: 'fff7ef7e-cb20-4fb2-a93b-c5139463c6bf', variable: 'GITHUB_TOKEN')]) {
          sh '''
            branch_python_mapping="${WORKSPACE}/branch-to-python-version.json"
            curl -s -o "${branch_python_mapping}" "https://${GITHUB_TOKEN}@raw.githubusercontent.com/inmanta/irt/master/branch-to-python-version.json"
            python_binary=$(/opt/irt/bin/irt get-python-version-for-checkout --map-file "${branch_python_mapping}" --path "${WORKSPACE}/inmanta-extension-template" 2>/dev/null || true)
            if [ -z "${python_binary}" ]; then
                python_binary=$(python3 -c "import json,os; m=json.load(open('${branch_python_mapping}')); print(m.get(os.environ.get('BRANCH_NAME',''), '') or 'python3')")
            fi
            ${python_binary} -m venv ${WORKSPACE}/env
            source ${WORKSPACE}/env/bin/activate
            pip install -c ${WORKSPACE}/inmanta-extension-template/requirements.txt cookiecutter
            # This creates an Inmanta extension project called 'project'
            cookiecutter --no-input ${WORKSPACE}/inmanta-extension-template
          '''
        }
      }
    }
    stage("Install test dependencies"){
      steps{
        sh '''
          source ${WORKSPACE}/env/bin/activate
          pip install -c ${WORKSPACE}/project/requirements.txt ${WORKSPACE}/project[dev]
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
