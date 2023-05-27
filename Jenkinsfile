pipeline{
    agent any
    environment{
        CC = "clang"
    }
    stages {
        stage("Example"){
            environment{
                DEBUG_FLAGS = '-g'
            }
            steps {
                dash "'${CC} $DEBUG_FLAGS"
                echo "========================"
                dash 'printenv'
            }
        }
    }
}
