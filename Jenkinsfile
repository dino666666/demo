node{
    stage("test"){
        withPythonEnv('/usr/bin/python3.10'){ // 填写刚刚在设置python路径时的名称
            sh "python3.10 --version"
            sh "python3.10 debug.py"
        }
    }
}