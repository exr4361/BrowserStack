 pipeline {
   agent any
   stages {
         stage('setup') {
           steps {
             browserstack(credentialsId: 'BS_Creds') {
                 echo 'hello bs'
            }
            browserStackReportPublisher 'automate'
           
            sh 'pip3 install -r requirements.txt --user'
            sh 'pip3 install urllib3==1.26.6 --user'
            sh 'python3 browserstechchallenge.py'
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
