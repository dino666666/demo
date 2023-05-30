pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo ""// 检出代码步骤
                // ...
            }
        }

        stage('Build') {
            steps {
                echo ""
                // 构建步骤
                // ...
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pwd'
                sh '(python3.10 debug.py)'
                //sh '(python3.10 -m pytest debug.py -s -q --alluredir ${WORKSPACE}/allure-results)'
                // 运行测试步骤
                // ...
            }
        }

        stage('Generate Allure Report') {
            steps {
                // 生成Allure报告步骤
                allure([
                    includeProperties: false,
                    jdk: '/usr/bin/java',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    report: 'allure-report',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}
