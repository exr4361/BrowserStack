 pipeline {
   agent any
   stages {
         stage('setup') {
           steps {
             browserstack(credentialsId: 'ca55402a-4065-406b-bf9c-0945c60c487d') {
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
             withCredentials([[
                $class: 'UsernamePasswordMultiBinding',
                credentialsId: 'ebbaffb3-eb51-465c-bb0b-6c72e19f477d',
                usernameVariable: 'trialuser',
                passwordVariable: 'trialpw',
             ]]) {
              sh '''
                    export BS_USR= %trialuser%
                    export BS_PW= %trialpw%
                    python3 browserstechchallenge.py
                 '''
             }
          }
       }
     }
   }
