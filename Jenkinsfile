 
node {
    def app

    

    
        stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        sh "docker build -t pca:latest ." 
    }
    

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        sh "python /tests/test_calcCovar.py"
        
    }
    stage('Deliver') { 
            sh "docker run -v ${PWD}src/Train:/usr/src/pca/Train pca" 
            
        }

    
}