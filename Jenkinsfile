 pipeline {
   agent any
   stages {
         stage('setup') {
          environment {
                   BS_Credentials = credentials('Trial')
               }
           steps {
             browserstack(credentialsId: 'BS_Creds') {
                 echo 'hello bs'
                 sh 'pip3 install -r requirements.txt --user'
                 sh 'pip3 install urllib3==1.26.6 --user'
                 sh 'python3 browserstechchallenge.py' 
             }
             browserStackReportPublisher 'automate'
           }
         }
       }
     }
   
