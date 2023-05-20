pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/droyb/world_of_games.git']]])
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        
        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        
        stage('Test') {
            steps {
                sh 'sleep 10'
                sh 'python tests/e2e.py'
            }
        }
        
        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                withCredentials([usernamePassword(credentialsId: '7af43511-4004-4cd8-a542-9d1fc312f4ab', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker-compose build world_of_games'
                    sh 'docker-compose push world_of_games'
                }
            }
        }
    }
}
