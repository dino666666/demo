'''

1.安装pytest和allure-pytest
    -pip3 install pytest
    -pip3 install allure-pytest
2.安装JDK即Java8
    -sudo apt-get install openjdk-8-jdk (java8)
    -sudo apt install openjdk-11-jdk   (java11)
3.下载allure并配置
    -https://github.com/allure-framework/allure2/releases
        -wget https://github.com/allure-framework/allure2/releases/download/2.22.1/allure-2.22.1.tgz
        -zhanghan@zhanghan-virtual-machine:/opt/allure-2.22.1$ tar xfz allure-2.22.1.tgz
        -zhanghan@zhanghan-virtual-machine:/opt/allure-2.22.1$ mv allure-2.22.1 /opt
    -添加环境变量： vi /etc/profile ==>最后一行添加 export PATH=/opt/allure-2.22.0/bin:$PATH
    -zhanghan@zhanghan-virtual-machine:/opt/allure-2.22.1$ source /etc/profile
4.运行
    -产生json文件：pytest.main(['-s', '-v', 'allure_study/test_demo.py', '-q', '--alluredir', './report'])
    -将json转成html：os.popen("allure generate report -o report/allure_reports/ --clean").read()

'''
