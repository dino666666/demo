'''

1.安装pytest和allure-pytest
    -pip install pytest
    -pip install allure-pytest
2.安装JDK即Java8
    -sudo apt-get install openjdk-8-jdk (java8)
    -sudo apt install openjdk-11-jdk   (java11)
3.下载allure并配置
    -https://github.com/allure-framework/allure2/releases
    -添加环境变量： vi /etc/profile ==>最后一行添加 export PATH=/opt/allure-2.22.0/bin:$PATH
4.运行
    -产生json文件：pytest.main(['-s', '-v', 'allure_study/test_demo.py', '-q', '--alluredir', './report'])
    -将json转成html：os.popen("allure generate report -o report/allure_reports/ --clean").read()

'''
