pipeline {
  agent any
  stages {
    stage('message') {
      steps {
        echo 'HELLO WORLD'
      }
    }

    stage('') {
      steps {
        mail(subject: 'Hello world', body: 'pokus', from: 'czechtechgeek@gmail.com', to: 'luke.lee@centrum.cz')
      }
    }

  }
}