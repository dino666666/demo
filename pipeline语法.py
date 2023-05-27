'''

1.Groovy语法
    1).定义变量
        -def x="adb" 、def y=1
    2).定义函数_命名参数
        def createName(String givenName, String familyName){
            return givenName + " " + familyName
        }
        调用：createName familyName="Lee", givenName="Bruce"
    3).定义函数_默认参数
        def sayHello(String name="humans"){
            print "hello ${name}"
        }
        调用：sayHello()
    4).单引号和双引号区别
        -双引号支持插值
            def name="world"
            print  "hello ${name}"   //hello world
            print   'hello ${name}'  //hello ${name}
2.pipeline最简结构
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
    1）pipeline：表示整条流水线的逻辑
    2）stage：流水线的阶段，至少有一个
    3）stages: 多个流水线阶段的容器
    4）steps：多个流水线阶段具体步骤的容器，一个stage中有且只有一个steps
    5）agent：指定流水线执行的具体位置
    以上都是必须的，少一个都会报错
3.post部分
    在pipeline结束后执行的动作，常用的就是发送邮件
    post{
        failure{
            mail to: '798255210@qq.com', subject: 'The Pipeline failed:'
        }
    }
    post部分的控制语句为：
    1）always：不论当前完成状态是什么，都执行
    2）hanged：只要当前完成状态与上一次完成状态不同就执行
    3）fixed：上一次完成状态为失败或不稳定（unstable），当前完成状态为成功时执行
    4）regression：上一次完成状态为成功，当前完成状态为失败、不稳定或中止（aborted）时执行
    5）aborted：当前执行结果是中止状态时（一般为人为中止）执行
    6）failure：当前完成状态为失败时执行
    7）success：当前完成状态为成功时执行
    8）unstable：当前完成状态为不稳定时执行。
    9）cleanup：清理条件块。不论当前完成状态是什么，在其他所有条件块执行完成后都执行







'''
