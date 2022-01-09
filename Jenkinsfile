pipeline {
    agent none
    stages {

        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }

            steps {
                sh 'py.test --junit-xml test-reports/results.xml tests/test_hello_world.py' 
            }
        }

         stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python main.py'
        
            }
         }
        
            
        
    }
}