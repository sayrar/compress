from PCA import PCA
import os
import numpy as np
import matplotlib.pyplot as plt


def load_data(input_dir):
    fnames = os.listdir(input_dir)
    print(1)
    fnames.sort()
    images = np.array([plt.imread(os.path.join(input_dir, fname)) for fname in fnames])
    images = images.T

    #Turning the array into a ( pixel size X num_samples ) size array
    new_arr = images.reshape(np.size(images,0)*np.size(images,1), -1)
	
	
    return new_arr.astype(float)
def rescale_images(reconst):
    #Rescaling the images to be in the range 0-255
    minVal = np.amin(reconst)
    maxVal = np.amax(reconst)
    reconst = reconst +-(minVal)
    reconst = reconst * (255/(maxVal-minVal))
    return reconst
def save_images(reconst):

    if not os.path.exists('Output'):
        os.makedirs('Output')
    for i in range(np.size(reconst,1)):
        img = reconst[:,i].reshape(48,60)
        img = img.T
        ext=".png"
        #plt.imsave(outstr, img,cmap='gray',format='png')
        plt.imsave(os.path.join("Output", str(i) + ext), img,cmap='gray',format='png')

def compress_images(DATA,k):
    pca = PCA(DATA, k)

    reconst = pca.perform_PCA()

    reconst = rescale_images(reconst)
    
    save_images(reconst)