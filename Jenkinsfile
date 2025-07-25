pipeline {
    agent any

    environment {
        IMAGE_NAME = "agandemajesty/my_django_project"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Clone Repo') {
    steps {
        git branch: 'main', url: 'https://github.com/Agandemajesty/MyDjangoProject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                }
            }
        }
    }
}