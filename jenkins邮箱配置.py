'''

1.jenkins插件安装
    -Email Extension
    -Email Extension Template

2.添加证书
    进入Manage Jenkins -> 凭据 -> 系统
    1)添加凭据
        范围： 全局
        用户名： zhanghanyxx@163.com
            Treat username as secret： 取消勾选
        密码：163填生成的密码/公司直接用密码
        ID： zhanghanyxx

3.jenkins邮箱配置
    进入Manage Jenkins -> Configure System
    1)配置管理员邮箱地址Jenkins Location
        系统管理员邮件地址： zhanghanyxx@163.com

    2)配置邮箱服务器Extended E-mail Notification
        SMTP server：smtp.163.com
        SMTP Port：465
            高级：
            Credentials：zhanghanyxx@163.com（提前添加证书）
            Use SSL: 打勾

        Default user e-mail suffix： @163.com
        Default Content Type： HTML
        Default Recipients： zhanghanyxx@163.com
        Reply To List：zhanghanyxx@163.com

    3)配置邮件通知
        SMTP服务器： smtp.163.com
        用户默认邮件后缀： @163.com
            高级：
                使用SMTP认证: 打勾
                    用户名： zhanghanyxx@163.com
                    密码： 163填生成的密码/公司直接用密码
                使用SSL协议：打勾
                Use TLS：打勾
                SMTP端口：465
                Reply-To Address：zhanghanyxx@163.com

4.pipeline最简单的邮件格式
    pipeline {
        agent any
        stages {
            stage('Hello') {
                steps {
                    echo 'Hello, Jenkins!'
                }
            }
        }
        post {
            always {
                emailext (
                    subject: "Jenkins pipeline (${env.JOB_NAME}) run result",
                    body: "Check console output at ${env.BUILD_URL}",
                    to: 'zhanghanyxx@163.com'
                )
            }
        }
    }

'''