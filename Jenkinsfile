pipeline{
    agent any
    withPythonEnv('/usr/bin/python3.10'){
        sh 'python3.10 --version'
    }
    stages {
        stage("Example"){
            steps {
                echo "Running ${env.BUILD_NUMBER} on ${env.JENKINS_URL}"
            }
        }
    }
}