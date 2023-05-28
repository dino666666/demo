pipeline{
    agent any

    stages {
        stage("Example"){
            withPythonEnv('/usr/bin/python3.10'){
                sh 'python3.10 --version'
            }
            steps {
                echo "Running ${env.BUILD_NUMBER} on ${env.JENKINS_URL}"
            }
        }
    }
}