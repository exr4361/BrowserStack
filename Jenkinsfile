 pipeline {
   agent any
   stages {
         stage('setup') {
           steps {
             browserstack(credentialsId: 'ca55402a-4065-406b-bf9c-0945c60c487d') {
                 echo 'hello bs'
            }
             withCredentials([[
                $class: 'UsernamePasswordMultiBinding',
                credentialsId: 'ebbaffb3-eb51-465c-bb0b-6c72e19f477d',
                usernameVariable: 'email',
                passwordVariable: 'pass',
            ]])
           }
          }
        stage('version') {
          steps {
             sh 'python3 --version'
           }
         }
        stage('test') {
          steps {
              sh """
                    export BS_USER="${email}"
                    export BS_PASS="${pass}"
                    python3 browserstechchallenge.py.py
                 """
          }
       }
     }
   }
