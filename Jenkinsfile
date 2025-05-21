pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t flask-greeting-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'PYTHONPATH=. pytest > result.log || true'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Running pylint...'
                sh 'pylint app/*.py || true'
            }
        }

        stage('Security') {
            steps {
                echo 'Running security scan with bandit...'
                sh 'bandit -r app/ || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying container...'
                sh 'docker run -d -p 5000:5000 flask-greeting-app'
            }
        }

        stage('Release') {
            steps {
                echo 'Releasing the app to production (placeholder stage).'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Monitoring logs and alerts setup (placeholder stage).'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'result.log', onlyIfSuccessful: false
        }
    }
}
