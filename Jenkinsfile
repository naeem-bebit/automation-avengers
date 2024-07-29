pipeline {
  environment {
    dockerimagename = "abidzar/automation-avangers"
    dockerImage = ""
  }
  agent any
  stages {
    stage('Checkout Source') {
      steps {
        git branch: 'k8s-deployment', url: 'https://github.com/naeem-bebit/automation-avengers'
      }
    }
    stage('Build image') {
      steps{
        script {
            sh "docker build . -t ${env.dockerimagename}:latest"
        }
      }
    }
    stage('Test') {
        steps {
            script {
                sh  "docker run --rm --tty --name avangers ${env.dockerimagename}:latest sh -c 'python ./tests/test_app.py'"
            }
        }
    }
    stage('Pushing Image') {
      environment {
          registryCredential = 'dockerhub-credentials'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            sh "docker push ${env.dockerimagename}:latest"
          }
        }
      }
    }
    stage('Deploying container to Kubernetes') {
      steps {
        script {
            withKubeConfig([credentialsId: 'k8s-lke']){
                sh "kubectl apply -f k8s-deployment.yml"
            }
        }
      }
    }
  }
}