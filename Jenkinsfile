 
node {
    def app

    

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build "pca"
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        sh "echo 'Test?'"
        
    }
    stage('Deliver') { 
            sh "docker run -v /:/usr/src/pca/Train pca:latest" 
            
        }

    
}