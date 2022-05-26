pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
               checkout scm
            }
        }
        stage('Build'){
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps{
            echo 'Build requirements'
            sh 'virtualenv venv --distribute'
            sh '. venv/bin/activate'
            sh 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image'){
            steps{
            echo 'Build Image'
            sh 'docker-compose build'
            }
        }

        stage('Test') {
            steps {
                // Test steps
                echo 'Testing Project...'
                sh 'docker-compose run app sh -c "python manage.py test"'
            }
        }
        stage('Deploy to Dockerhub') {
            steps {
                // Deploy steps
                echo 'Deploying to hub'

                sh """
                docker login -u franciswilliams -p 242477366
                docker build -t franciswilliams/percom_garage:latest
                docker push franciswilliams/percom_garage:latest
                """
            }
        }
    }
}