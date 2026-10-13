
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Build') {
            steps {
                bat '"C:\\Users\\PRANES T\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m compileall -q src tests'
                echo 'Build completed successfully.'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\PRANES T\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest discover -s tests -v'
            }
        }

        stage('Result') {
            steps {
                echo 'Build and test stages completed successfully!'
            }
        }
    }

    post {
        success {
            echo 'PIPELINE RESULT: SUCCESS'
        }
        failure {
            echo 'PIPELINE RESULT: FAILURE'
        }
        always {
            echo 'Jenkins pipeline execution finished.'
        }
    }
}
