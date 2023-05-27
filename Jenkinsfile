pipeline{
    agent any
    stages {
        stage("Example"){
            steps {
                echo "Running ${env.BUILD_NUMBER} on ${env.JENKINS_URL}" //推荐方法一
                echo "Running $env.BUILD_NUMBER on $env.JENKINS_URL" //推荐方法二
                echo "Running ${BUILD_NUMBER} on ${JENKINS_URL}" //不推荐方法三
                sh 'printenv'
            }
        }
    }
}
