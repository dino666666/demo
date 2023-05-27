pipeline{
    agent any
    stages {
        stage("Build"){
            steps {
                echo "hello world"
            }
        }
    }
    post{
    failure{
        mail to: '798255210@qq.com', subject: 'The Pipeline failed:'
        }
    }
}
