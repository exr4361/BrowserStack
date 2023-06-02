 pipeline {
   agent any
   stages {
         stage('setup') {
           steps {
             browserstack(credentialsId: 'ca55402a-4065-406b-bf9c-0945c60c487d) {
                 echo 'hello bs'
            }
           }
          }
        stage('version') {
          steps {
             sh 'python3 --version'
           }
         }
        stage('test') {
          steps {
              sh 'python3 browserstechchallenge.py'
          }
       }
     }
   }
