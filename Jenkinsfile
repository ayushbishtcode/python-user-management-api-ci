pipeline {

    agent any

    environment {
           IMAGE_NAME = "python-user-management-api"
           IMAGE_TAG = "latest"
           DOCKER_USERNAME = "YOUR_DOCKER_USERNAME"
    }

    stages {
        
    }

    post {

        success {
            echo "pipeline executed successfully."
        }

        failure {
            echo "pipeline failed"
        }

        always {
            echo "pipeline execution finished"
        }

    }

}