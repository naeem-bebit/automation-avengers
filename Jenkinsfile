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
            dockerImage = docker.build("${env.dockerimagename}:${env.BUILD_ID}")
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
            sh "cat k8s-deployment.yml.tmpl | sed 's/\\\$build_id/${env.BUILD_ID}/g' > k8s-deployment.yml.tmpl"
            sh "cat k8s-deployment.yml.tmpl | sed 's/\\\$dockerimagename/${env.dockerimagename}/g' > k8s-deployment.yml"
            withKubeConfig([credentialsId: 'k8s-lke']){
                sh "kubectl apply -f k8s-deployment.yml"
                sh "kubectl rollout restart deployment web-app-deployment"
                sh "kubectl describe deploy web-app-deployment "

            }
        }
      }
    }
  }
}