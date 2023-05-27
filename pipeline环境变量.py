'''

1.Jenkins内置变量
    pipeline{
        agent any
        stages {
            stage("Example"){
                steps {
                    echo "Running ${env.BUILD_NUMBER} on ${env.JENKINS_URL}" //推荐方法一
                    echo "Running $env.BUILD_NUMBER on $env.JENKINS_URL" //推荐方法二
                    echo "Running ${BUILD_NUMBER} on ${JENKINS_URL}" //不推荐方法三
                    sh'printenv' //小技巧，打印env的熟悉值
                }
            }
        }
    }
    1)BUILD_NUMBER: 构建号，累加的数字
    2)BRANCH_NAME: 多分支pipeline项目支持
    3)BUILD_URL: 当前构建的页面URL.可以把链接放在邮件通知中
    4)GIT_BRANCH： 通过git拉取的源码构建的项目才会有此变量
    5）自定义变量：












'''