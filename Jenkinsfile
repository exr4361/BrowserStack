 pipeline {
   agent any
   stages {
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
