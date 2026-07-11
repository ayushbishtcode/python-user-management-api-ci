pipeline {

    agent any

    environment {
        IMAGE_NAME = "python-user-management-api"
        IMAGE_TAG = "latest"
        DOCKER_USERNAME = "ayushbishtt"    // Replace with your Docker Hub username
    }

    stages {

        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest -v
                '''
            }
        }

        stage('Check Docker') {
            steps {
                sh '''
                    export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
                    echo "PATH=$PATH"
                    which docker
                    docker --version
                    docker ps
                 '''
             }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

                    docker build \
                    -t ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
                        
                        echo "$DOCKER_PASS" | docker login \
                            -u "$DOCKER_USER" \
                            --password-stdin

                        docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}

                        docker logout
                    '''
                }
            }
        }

    } // <-- stages block ends here

    post {

        success {
            echo "✅ Pipeline executed successfully."
        }

        failure {
            echo "❌ Pipeline failed."
        }

        always {
            echo "Pipeline execution finished."
        }
    }
}