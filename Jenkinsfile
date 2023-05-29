pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // 检出代码步骤
                // ...
            }
        }

        stage('Build') {
            steps {
                // 构建步骤
                // ...
            }
        }

        stage('Run Tests') {
            steps {
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
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}
