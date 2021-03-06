pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    options {
        // Only keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr:'10'))
    }
    stages {
//         stage('Start Notifications') {
//             agent {
//                 label 'docker'
//              }
//             steps {
//                 // send build started notifications
//                 sendNotifications 'STARTED'
//             }
//         }
        stage('Git Checkout') {
            steps {
               checkout scm
            }
        }
        stage('Build'){
            agent {
                docker {
                    image 'python:3.8.13-alpine3.16'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]) {
                  sh "pip install virtualenv"
                  sh "virtualenv venv"
                  sh "pip install -r requirements.txt "
                  //sh "docker run -u 0 --privileged --name jenkins -it -d -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /home/jenkins_home:/var/jenkins_home jenkins/jenkins"
                }
            }
        }
        stage('Build Docker Image'){
            agent {
                docker {
                    label 'docker'
                        image 'slopresto/jenkins-docker-agent:latest'
//                         args '-v /var/run/docker.sock:/var/run/docker.sock -u jenkins'
                 }
            }
            steps{
            echo 'Build Image'
            sh 'docker-compose build'
            }
        }

        stage('Test') {
            agent {
                docker {
                    label 'docker'
                        image 'slopresto/jenkins-docker-agent:latest'
//                         args '-v /var/run/docker.sock:/var/run/docker.sock -u jenkins'
                 }
            }
            steps {
                // Test steps
                echo 'Testing Project...'
                sh 'docker-compose run app sh -c "python manage.py test"'
            }
        }
        stage('Deploy to Dockerhub') {
            agent {
                    dockerfile true }
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
    post {
        always {
            sendNotifications currentBuild.result
        }
    }
}