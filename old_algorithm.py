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

def calcPSNR(image_true, image_test):
    mse = np.mean((image_true - image_test)**2)
    if(mse == 0):
        return 100
    max_pixel = 255.
    val_psnr = 20 * (log10(max_pixel/sqrt(mse)))
    return val_psnr

def calcSSIM(image_true, image_test):
    val_ssim = skimage.metrics.structural_similarity(image_true, image_test)
    return val_ssim

def compression(comp, size):

    levels = int(((100. - comp)/100.)*(size*size))

    return levels

def algo(s,l,path):
    
    
    size = s
    #levels = int(((100. - compression)/100.)*(size*size))

    levels = l
    #print(levels)
    if levels == 0:
        levels = 1

    img = imageAcquisition(path)
    img = img.astype(np.float32)
    img_new = np.zeros((img.shape[0],img.shape[1]), dtype=np.float32)

    for i in range(img.shape[0]//size):
        for j in range(img.shape[1]//size):
            img_block = getBlocks(img,i,j,size)

            max_img = np.amax(img_block)
            min_img = np.amin(img_block)

            diff = (max_img - min_img)
            bin_val = diff/levels

            for m in range(size):
                for n in range(size):
                    if diff != 0:
                        img_new[m+(i*size),n+(j*size)] = ((((img_block[m,n] - min_img)//bin_val) + 1)*bin_val) + min_img
                    else:
                        img_new[m+(i*size),n+(j*size)] = min_img

    #print(img)
    #print(img_new)
    print('PSNR of Thresholded Image : '+str(calcPSNR(img, img_new)))

    
if __name__ == "__main__":

    path = 'res/thermal.png'
    sizes = np.array([8, 16, 32])
    levels = np.array([4,8,12,16,20])

    for i in range(sizes.shape[0]):
        print("The block size is : %d"%sizes[i])
        for j in range(levels.shape[0]):
            algo(sizes[i],levels[j],path)
        print()
    
