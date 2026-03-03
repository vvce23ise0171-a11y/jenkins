pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/vvce23ise0171-a11y/jenkins.git',
                    branch: 'main'
            }
        }

        stage('Run Python') {
            steps {
                sh 'python3 script.py'
            }
        }
    }
}
