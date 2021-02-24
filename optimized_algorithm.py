import os
import cv2
import copy
import skimage
import numpy as np
from math import log10, sqrt
from pathlib import Path
import matplotlib.pyplot as plt

def imageAcquisition(path):
    img = cv2.imread(path, 0)
    return img

def getBlocks(img, i, j, size):
    
    #get the block of the image
    b_img = np.zeros((size,size), dtype=np.float32)
    b_img  = img[(size*i):(size*i)+size,(size*j):(size*j)+size]
    return b_img

def displayImage(ax,img,title):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')
    #plt.imsave('res/processed_image.png',img,cmap='gray')
    #plt.imshow(img, cmap='gray')
    #plt.show()
    return None

def calcPSNR(image_true, image_test):
    mse = np.mean((image_true - image_test)**2)
    if(mse == 0):
        return 100
    max_pixel = 255
    val_psnr = 20 * (log10(max_pixel/sqrt(mse)))
    return val_psnr

def calcSSIM(image_true, image_test):
    val_ssim = skimage.metrics.structural_similarity(image_true, image_test)
    return val_ssim

def plotHistograms(img,i,j,k):
    
    plt.subplot(i, j, k)
    plt.hist(img.ravel(),256,[0,256])

    plt.xlabel('Intensity (0-255)')
    plt.ylabel('Count (Nos.)')
    plt.title('Intensity histogram for the test image.')
    plt.show()

    return None

if __name__ == "__main__":

    #levels define the new threshold levels
    #size defines the block size to be extracted
    levels = 4
    size = 128

    #obtain the image
    #create a new container for the image
    path = 'res/img_08.tif'
    img_a = imageAcquisition(path)

    #define the figures that are to be generated
    plt.figure()
    ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2)
    ax2 = plt.subplot2grid((3, 2), (1, 0))
    ax3 = plt.subplot2grid((3, 2), (1, 1))
    ax4 = plt.subplot2grid((3, 2), (2, 0))
    
    ax1.hist(img_a.ravel(),256,[0,256])
    displayImage(ax2,img_a,'Original Image')
    
    #converting the scale tp (0-1000mv)
    img = img_a/255.
    img_new = np.zeros((img.shape[0],img.shape[1]), dtype=np.float32)
    img_new_mov = np.zeros((img.shape[0],img.shape[1]), dtype=np.float32)
    
    #get the 8X8 images
    #at each 8X8 blocks find the min and the max
    for i in range(img.shape[0]//size):
        for j in range(img.shape[1]//size):
            img_b = getBlocks(img, i, j, size)
            img_b_mov = copy.deepcopy(img_b)
            
            #number of bins for the pseudo compression
            #find the maxium and minimum values from the patch
            max_img = np.amax(img_b) 
            min_img = np.amin(img_b)
            
            img_b_mov = img_b_mov - min_img 

            #redundant code
            diff = max_img - min_img 
            bins = diff / levels
            
            #creating thresholds relating to actual conversion
            #filling in the values in the 
            for k in range(size):
                for l in range(size): 
                    if bins != 0:
                        img_new[k+(i*size),l+(j*size)] = int((img_b[k,l] - min_img)/bins)*bins + min_img
                        #check this logic
                        img_new_mov[k+(i*size),l+(j*size)] = img_b_mov[k,l]
                    else:
                        img_new[k+(i*size),l+(j*size)] = max_img
                        img_new_mov[k+(i*size),l+(j*size)] = img_b_mov[k,l]
    
    #carry out similarity quantification
    max_img = np.amax(img_new)
    min_img = np.amin(img_new)
    #img_new *= (255. / max_img)
    img_new *= 255.
    img_new_ = np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8)

    for i in range(img_new.shape[0]):
        for j in range(img_new.shape[1]):
            img_new_[i,j] = int(img_new[i,j])
    
    img_new_mov *= 255.
    img_new_mov_ = np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8)

    for i in range(img_new_mov.shape[0]):
        for j in range(img_new_mov.shape[1]):
            img_new_mov_[i,j] = int(img_new_mov[i,j])

    displayImage(ax3,img_new_,'Thresholded Image')
    displayImage(ax4,img_new_mov,'Shifted Image')
    print('PSNR of thresholded Image : '+str(calcPSNR(img_a, img_new_)))
    print('PSNR of shifted Image : '+str(calcPSNR(img_a, img_new_mov_)))
    plt.tight_layout() 
    plt.show()

