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
                echo ""
                // 运行测试步骤
                // ...
            }
        }
    post('Results') { // 执行之后的操作
        always{
            script{// 集成allure，目录需要和保存的results保持一致，注意此处目录为job工作目录之后的目录，Jenkins会自动将根目录与path进行拼接
                allure includeProperties: false, jdk: '/usr/bin/java', report: 'report/allure-report', results: [[path: 'report/allure-results']]
            }
        }
        //stage('Generate Allure Report') {
            //steps {
                // 生成Allure报告步骤
                //allure([
                //    includeProperties: false,
                //    jdk: '/usr/bin/java',
                //    properties: [],
                //    reportBuildPolicy: 'ALWAYS',
                 //   results: [[path: 'allure-results']]
                //])
            //}
    }
}
