'''

1.Pipeline: 就是用代码的方式部署项目流水线生产的过程

2.Jenkinsfile：所有部署流水线的代码都写在jenkinsfile中

3.如何安装pipline
    -【系统管理】->【插件管理】->【可选插件】，然后在搜索框输入 ”Pipeline“。安装

4.pipline语法
    -Groovy语法
    -最简结构：
# Jenkinsfile 文件
pipeline{
    agent any
    stages {
        stage("Build"){
            steps {
                echo "hello world"
            }
        }
    }
}

5.gitlab代码拉取
    -配置github的公钥
        -zhanghan@ubuntu:~$ cat .ssh/id_rsa.pub
    -配置Jenkins的私钥
        -zhanghan@ubuntu:~$ cat .ssh/id_rsa
    -配置Jenkins的Git
    -构建
        -构建中在工作空间中，如：/home/zhanghan/jenkins/workspace/ssh-credentials-demo
    -配置Jenkins脚本路径Jenkinsfile

'''