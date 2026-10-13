
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
                bat '"C:\\Users\\PRANES T\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"C:\\Users\\PRANES T\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest discover -s tests -v'
            }
        }
    }
}
