import copy
import os
from math import log10, sqrt
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage

def imageAcquisition(path):
    
    img = cv2.imread(path, 0)

    #converting values to normalized sensor range of (0 to 1000 mV)
    plt.imshow(img)
    #plt.show()
    return img

def getBlocks(img, i, j):
    b_img = np.zeros((size,size), dtype=np.float32)
    b_img  = img[(size*i):(size*i)+size,(size*j):(size*j)+size]
    return b_img

def displayImage(img):
    plt.imsave('res/processed_image.png',img,cmap='gray')
    plt.imshow(img, cmap='gray')
    plt.show()
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

if __name__ == "__main__":

    #levels (defined by the hardware)
    levels = 16
    size = 8    
    #obtain the image 
    path = 'res/img_08.tif'
    img_a = imageAcquisition(path)
    img = img_a/255.
    img_new = np.zeros((img.shape[0],img.shape[1]), dtype=np.float32)

    #get the 8X8 images
    for i in range(img.shape[0]//size):
        for j in range(img.shape[1]//size):
            img_b = getBlocks(img, i, j)

            #number of bins for the pseudo compression
            #find the maxium and minimum values from the patch
            max_img = np.amax(img_b) 
            min_img = np.amin(img_b)
            #print(max_img,min_img)
            
            #redundant code
            diff = max_img - min_img 
            bins = diff / levels
            #print(bins)
            #creating thresholds relating to actual conversion
            #filling in the values in the 
            for k in range(size):
                for l in range(size): 
                    if bins != 0:
                        img_new[k+(i*size),l+(j*size)] = int((img_b[k,l] - min_img)/bins)*bins + min_img
                    else:
                        img_new[k+(i*size),l+(j*size)] = max_img
    
    #carry out similarity quantification
    max_img = np.amax(img_new)
    min_img = np.amin(img_new)
    print(max_img,min_img)
    img_new *= (255. / max_img)
    img_new_ = np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8)
    for i in range(img_new.shape[0]):
        for j in range(img_new.shape[1]):
            img_new_[i,j] = int(img_new[i,j])
    print(img_new_)
    displayImage(img_new_)
    print(calcPSNR(img_a, img_new_))
    #print(calcSSIM(img, img_new))
