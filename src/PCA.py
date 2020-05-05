# -*- coding: utf-8 -*-
#def compress_images(DATA,k):
import matplotlib.pyplot as plt
import numpy as np

class PCA(object):
    def __init__(self,DATA, k):
        self.DATA = DATA
        self.k = k
        print(1)

    def standardize(self):

        x_bar = np.mean(self.DATA, axis =1).reshape(-1,1)
        self.Z =  self.DATA - x_bar
        return self.Z

    def calc_covar(self, Z):
        covar = np.matmul(Z, Z.T)

        return np.linalg.eig(covar)
    def sort_eig(self, eigenValues, eigenVectors):
        
        idx = eigenValues.argsort()[::-1]   
        
        eigenValues = eigenValues[idx]
        eigenVectors = eigenVectors[:,idx]

        eigenVectors = eigenVectors.real
        eigenValues = eigenValues.real

        return eigenVectors

    def project_Data(self, Z,U):
        Z_star = np.matmul(Z.T,U)
        reconst = np.matmul(Z_star, U.T)

        return  reconst.T
    def perform_PCA(self):
        self.Z = self.standardize()
    
        #Calculating the covariance matrix
        self.eigenValues, self.eigenVectors = self.calc_covar(self.Z)
    
    #   Sorting the eigenvectors corresponding to their eigenvalues
        eigenVectors = self.sort_eig(self.eigenValues, self.eigenVectors)
    
       #Keeping only the k most important features
        self.U = eigenVectors[:,0:self.k]
        reconst = self.project_Data(self.Z, self.U)
        return reconst

    




    
    


    
    
    
    


