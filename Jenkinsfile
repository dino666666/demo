pipeline{
    agent any
    environment{
        CC = 'clang'
    }
    stages {
        stage("Example"){
            environment{
                DEBUG_FLAGS = '-g'
            }
            steps {
                sh "${CC} ${DEBUG_FLAGS}"
                sh 'printenv'
            }
        }
    }
}
