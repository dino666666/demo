'''

环境总结

1.pipeline 脚本环境:
    -Jenkinsfile文件内容
        pipeline {
            agent any

            stages {
                stage('auto test') {
                    steps {
                        sh 'python3 debug.py'
                    }
                }
            }
            post {
              success {
                // 注意报告地址写相对路径，也就是--alluredir后面的路径,如我的报告路径：report/allure_raw，但不要写成 /report/allure_raw
                allure includeProperties: false, jdk: 'jdk1.8', results: [[path: 'report/allure_raw']]
              }
            }
        }
    -debug.py文件内容
        import sys
        import os
        sys.path.append("/var/lib/jenkins/.local/lib/python3.10/site-packages")
        print(sys.path)
        import pytest
        if __name__ == "__main__":
             pytest.main(['-s', '-v', 'test_demo.py', '-q', '--alluredir=report/allure_raw'])

2.jenkins 默认用户设置:
    -修改默认用户密码
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo passwd jenkins
    -将默认用户添加到用户组
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG sudo jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG root jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG zhanghan jenkins
        ===========如果遇到其他未知问题再往下执行（未验证）==========
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG adm jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG cdrom jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG dip jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG plugdev jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG lpadmin jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG lxd jenkins
        zhanghan@zhanghan-virtual-machine:~/下载$ sudo usermod -aG sambashare jenkins

3.jenkins默认用户工具环境
    -allure-pytest重新下载
        jenkins@zhanghan-virtual-machine:/home/zhanghan/Downloads/tmp$ pip3 install allure-pytest
    -查看python三方包的pythonpath
        -即重安装一次pytest
        jenkins@zhanghan-virtual-machine:/home/zhanghan/Downloads/tmp$ pip3 install pytest
            //Requirement already satisfied: pytest in /var/lib/jenkins/.local/lib/python3.10/site-packages (7.3.1)
        -将pythonpath添加到sys.path中
            sys.path.append("/var/lib/jenkins/.local/lib/python3.10/site-packages")
    -allure环境变量启动
        jenkins@zhanghan-virtual-machine:/opt/allure-2.22.1/bin$ vim /etc/profile
            //检查是否添加export PATH=/opt/allure-2.22.1/bin:$PATH
        jenkins@zhanghan-virtual-machine:/opt/allure-2.22.1/bin$ source /etc/profile

4.Pipeline script from SCM设置
    -定义：Pipeline script from SCM
    -SCM： Git
    -Repository URL： git@github.com:dino666666/tmp.git
    -Credentials： dino666666_2
        -进入系统管理-Credentials-System-全局凭据-Add Credentials
            -范围： 全局（Jenkins， nodes， items， all child items， etc）
            -ID：zh-2 （随便写）
            -Username： dino666666_2 （随便写）
            -Treat username as secret： 取消勾选
            -Private Key-Enter directly-Key： 添加私钥cat ~/.ssh/id_rsa
            -Passphrase： 空着（ssh密钥的密码）
    -Branches to build: */master
    -脚本路径: Jenkinsfile
    -轻量级检出: 勾选

5.全局工具设置
    -JDK
        -别名： java
        -JAVA_HOME： /usr/lib/jvm/java-11-openjdk-amd64
            #路径查看方法
            -jenkins@zhanghan-virtual-machine:/$ ls -l /usr/bin/java
            lrwxrwxrwx 1 root root 22  6月  4 16:03 /usr/bin/java -> /etc/alternatives/java
            -jenkins@zhanghan-virtual-machine:/$ ls -l /etc/alternatives/java
            lrwxrwxrwx 1 root root 43  6月  4 16:03 /etc/alternatives/java -> /usr/lib/jvm/java-11-openjdk-amd64/bin/java
        -自动安装： 取消勾选
    -Git installations-Git
        -Name：git
        -Path to Git executable：/usr/bin/git
        -自动安装： 取消勾选
    -Allure Commandline
        -别名: allure
        -安装目录:/opt/allure-2.22.1
        -自动安装： 取消勾选

6.目标模板
    https://www.jianshu.com/p/af1eb503eb4a

'''