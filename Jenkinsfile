
pipeline {
    agent any
    stages {
        stage('Checkout Source') {
          steps {
            checkout scm
          }
        }
        stage('Check Python Installations'){
            steps{
                withPythonEnv('python3') {
                    sh 'echo "Installed Python versions"'
                    sh 'echo "$(pyenv versions)"'
                    sh 'echo "Using Python version"'
                    sh 'echo "$(python3 --version)"'
                }
            }
        }
        stage('Install Dependencies') { 
            steps {
                withPythonEnv('python3') {

                    sh 'pip install --no-cache-dir -r requirements.txt' 
                }
            }
        }
        stage('Run App Test') { 
            steps {
                withPythonEnv('python3') {
                    sh 'python tests/test_app.py' 
                }
            }
        }
    }
}
