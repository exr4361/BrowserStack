 pipeline {
   agent any
   stages {
         stage('setup') {
           steps {
             environment {
               BS_Credentials = credentials('Trial')
             }
             browserstack(credentialsId: 'BS_Creds') {
                 echo 'hello bs'
                 sh 'pip3 install -r requirements.txt --user'
                 sh 'pip3 install urllib3==1.26.6 --user'
                 export BS_USR=${BS_Credentials_USR}
                 export BS_PW=${BS_Credentials_PSW}
                 sh 'python3 browserstechchallenge.py' 
            }
            browserStackReportPublisher 'automate'
           }
          }
       }
     }
   }
