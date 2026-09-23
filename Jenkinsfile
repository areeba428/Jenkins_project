pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker rm -f mlops-container || true
                    docker run -d -p 5000:5000 --name mlops-container mlops-flask-app
                '''
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline finished.'
        }
    }
}