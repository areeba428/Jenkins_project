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
                bat 'docker build -t mlops-flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                    docker rm -f mlops-container 2>NUL || exit /b 0
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
