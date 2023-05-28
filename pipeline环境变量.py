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
                    sh 'printenv' //小技巧，打印env的熟悉值
                }
            }
        }
    }
    1)BUILD_NUMBER: 构建号，累加的数字
    2)BRANCH_NAME: 多分支pipeline项目支持
    3)BUILD_URL: 当前构建的页面URL.可以把链接放在邮件通知中
    4)GIT_BRANCH： 通过git拉取的源码构建的项目才会有此变量
    5）pipeline中自定义变量：---不能跨文件
        pipeline{
            agent any
            environment{
                _CC = 'clang'  //小技巧，这里最好加个前缀_避免变量名冲突
            }
            stages {
                stage("Example"){
                    environment{
                        DEBUG_FLAGS = '-g'
                    }
                    steps {
                        sh "${_CC} ${DEBUG_FLAGS}"
                        sh 'printenv'
                    }
                }
            }
        }
        上面的例子没跑通 //提示not found clang
    6）自定义全局环境变量---可以跨文件，因为是全局的
        -进入Manage Jenkins→Configure System→Global properties，勾选“Environment variables”复选框，单击“Add”按钮，
         在输入框中输入变量名和变量值即可

2.Python环境安装
    Python开发通常会进行工程级别的环境隔离，也就是每个Python工程使用一个Python环境
    1)ubuntu安装pyenv
        -root@zhanghan-virtual-machine:~# cd ~
        -root@zhanghan-virtual-machine:~# pwd
            /root
        -root@zhanghan-virtual-machine:~# git clone https://github.com/pyenv/pyenv.git ~/.pyenv
        -root@zhanghan-virtual-machine:~# ls -al
            drwxr-xr-x 12 root root 4096  5月 28 21:38 .pyenv
        -root@zhanghan-virtual-machine:~# vim ~/.bashrc
            添加export PYENV_ROOT="$HOME/.pyenv"
                export PATH="$PYENV_ROOT/bin:$PATH"
                eval "$(pyenv init --path)"
        -root@zhanghan-virtual-machine:~# source ~/.bashrc
        -root@zhanghan-virtual-machine:~# pyenv --version
            pyenv 2.3.18
    2)Jenkins安装pyenv插件
        -Dashboard-Manage Jenkins-插件管理-Available plugins





'''