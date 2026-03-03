pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/your-repo/your-python-project.git',
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
