pipeline {
  environment {
    dockerimagename = "naeem158/flask-web-app:latest"
    dockerImage = ""
  }
  agent any
  stages {
    stage('Checkout Source') {
      steps {
        git 'https://github.com/naeem-bebit/automation-avengers'
      }
    }
    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build dockerimagename
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
            dockerImage.push("latest")
          }
        }
      }
    }
    stage('Deploying container to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "k8s-deployment.yml")
        }
      }
    }
  }
}