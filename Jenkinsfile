pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }
    }
}
