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
            dockerImage = docker.build("${env.dockerimagename}:latest")
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
             dockerImage.push()
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