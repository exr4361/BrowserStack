 pipeline {
   agent any
   stages {
         stage('setup') {
           steps {
             browserstack(credentialsId: 'ca55402a-4065-406b-bf9c-0945c60c487d') {
                 echo 'hello bs'
            }
            sh 'pip3 install -r requirements.txt'
           }
          }
        stage('version') {
          steps {
             sh 'python3 --version'
           }
         }
        stage('test') {
           environment {
              BS_Credentials = credentials('Trial')
           }
          steps {
              sh '''
                    export BS_USR=${BS_Credentials_USR}
                    export BS_PW=${BS_Credentials_PSW}
                    python3 browserstechchallenge.py
                 '''
          }
       }
     }
   }
