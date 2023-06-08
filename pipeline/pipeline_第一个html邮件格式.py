'''


1.pipeline脚本：
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
                    subject: '${DEFAULT_SUBJECT}',
                    body: '${DEFAULT_CONTENT}',
                    to: '798255210@qq.com'
                )
            }
        }
    }

2.DEFAULT_CONTENT内容：
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style type="text/css">
            .title{
                text-align: center;
                color: rgb(0, 0, 0);
            }
            .desc{
                text-align: left;
            }
        </style>
    </head>
    <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
    <table width="95%" cellpadding="0" cellspacing="0" style="font-size: 16pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
        <div>
            <h1 class="title">稳定性自动化测试报告</h1>
        </div>
        <div class="desc">
            <p><font color="red">（Jenkins自动发送的测试报告邮件，无需回复！)</font></p>
            <h2>在线测试报告直达链接：<a href="${PROJECT_URL}${BUILD_NUMBER}/allure">${PROJECT_URL}${BUILD_NUMBER}/allure</a></h2>
        </div>
        <tr>
            <td><br />
            <b><font color="#0B610B"><font size="6">构建信息</font></font></b>
            <hr size="2" width="100%" align="center" /></td>
        </tr>
        <tr>
            <td>
                <ul>
                <div style="font-size:18px">
                    <li>构建名称：${PROJECT_NAME}</li>
                    <li>构建结果: <span style="color:green"> Successful </span></li>
                    <li>构建编号：${BUILD_NUMBER}</li>
                    <li>触发原因：${CAUSE}</li>
                    <li>部署分支：None </li>
                    <li>测试报告地址：<a href="${PROJECT_URL}${BUILD_NUMBER}/allure">${PROJECT_URL}${BUILD_NUMBER}/allure</a></li>
                    <li>环境: None </li>
                    <li>测试阶段：None </li>
                    <li>变更概要：None </li>
                    <li>变更集: None</li>
                    <li>构建地址：<a href=${BUILD_URL}>${BUILD_URL}</a></li>
                    <li>构建日志：<a href=${BUILD_URL}console>${BUILD_URL}console</a></li>
                </div>
                </ul>
            </td>
        </tr>
    </table>
    </body>
    </html>

============================================================在公司优化后============================================================





2.DEFAULT_CONTENT内容：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .title{
            text-align: center;
            color: rgb(0, 0, 0);
        }
        .desc{
            text-align: left;
        }
    </style>
</head>
<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
<table width="95%" cellpadding="0" cellspacing="0" style="font-size: 16pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
    <div>
        <h1 class="title">稳定性自动化测试报告</h1>
    </div>
    <div class="desc">
        <p><font color="red">（Jenkins自动发送的测试报告邮件，无需回复！)</font></p>
        <h2>在线测试报告直达链接：<a href="${PROJECT_URL}${BUILD_NUMBER}/allure">${PROJECT_URL}${BUILD_NUMBER}/allure</a></h2>
    </div>
    <tr>
        <td><br />
        <b><font color="#0B610B"><font size="6">构建信息</font></font></b>
        <hr size="2" width="100%" align="center" /></td>
    </tr>
    <tr>
        <td>
            <ul>
            <div style="font-size:18px">
                <li>构建名称：${PROJECT_NAME}</li>
                <li>构建结果: <span style="color:green"> Successful </span></li>
                <li>构建编号：${BUILD_NUMBER}</li>
                <li>触发原因：${CAUSE}</li>
                <li>部署分支：None </li>
                <li>测试报告地址：<a href="${PROJECT_URL}${BUILD_NUMBER}/allure">${PROJECT_URL}${BUILD_NUMBER}/allure</a></li>
                <li>环境: None </li>
                <li>测试阶段：None </li>
                <li>变更概要：None </li>
                <li>变更集: None</li>
                <li>构建地址：<a href=${BUILD_URL}>${BUILD_URL}</a></li>
                <li>构建日志：<a href=${BUILD_URL}console>${BUILD_URL}console</a></li>
            </div>
            </ul>
        </td>
    </tr>
</table>
</body>
</html>


'''
