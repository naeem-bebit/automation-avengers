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
    stage('Deploying container to Kubernetes') {
      steps {
        script {

            //sh """
            //    export dockerimagename=${env.dockerimagename}
            //    export build_id=${env.BUILD_ID}
            //    envsubst < k8s-deployment.yml.tmpl > k8s-deployment.yml
            //    """

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