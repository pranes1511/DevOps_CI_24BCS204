pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Checkout completed'
            }
        }

        stage('Build') {
            steps {
                bat '"C:\\Users\\PRANES T\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m compileall -q src tests'
                echo 'Build completed'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\PRANES T\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest discover -s tests -v'
            }
        }

        stage('Result') {
            steps {
                echo 'Pipeline completed successfully'
            }
        }

        stage('Finish') {
            steps {
                echo 'Jenkins pipeline finished'
            }
        }
    }
}
