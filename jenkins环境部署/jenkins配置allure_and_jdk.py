'''

Jenkins配置allure插件

    1.jenkins安装Allure插件
        -Manage Jenkins → 插件管理 → 搜索allure → 安装并重启jenkins
    2.jenkins配置allure命令行工具
        -Manage Jenkins → Tools → Allure Commandline
            -Name： allure-jiep2.22
            -安装目录： /opt/allure-2.22.1/
            -重要：取消勾选Install automatically
    3.jenkins配置Allure报告生成

Jenkins配置jdk插件
    1.进入Manage Jenkins → Tools → JDK
        -Name： java11
        -JAVA_HOME： /usr/lib/jvm/java-11-openjdk-amd64  可通过ls -l查看一层层软链接得到
        -重要：取消勾选Install automatically
    3.jenkins配置Allure报告生成




'''