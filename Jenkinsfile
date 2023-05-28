pipeline{
    agent any
    stages {
        stage("test"){
            withPythonEnv('/usr/bin/python3.10'){ // 填写刚刚在设置python路径时的名称
                sh "python3.10 --version"
                sh "pwd"
                //sh "python3.10 debug.py"
            }
        }
        stage("Example"){
            steps {
                echo "Running ${env.BUILD_NUMBER} on ${env.JENKINS_URL}" //推荐方法一
            }
        }
    }
}