# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:14:55 2019

@author: student
"""

import numpy as np
import cv2 as cv
import math as fn

#original = cv.imread(r"C:\Users\student\Desktop\Lichtenstein.jpg",0)
#
#scale_percent = 60 # percent of original size
#width = int(original.shape[1] * scale_percent / 100)
#height = int(original.shape[0] * scale_percent / 100)
#
#dim=(256,256)
#
#resized=cv.resize(original,dim,interpolation=cv.INTER_AREA)
#
#cv.imshow('castle',original)
#cv.imshow('scaled castle',resized)

image=np.array(([3,3],
                [3,3]), dtype="uint8")

N=image.shape[0]
M=image.shape[1]
DFT_Image=np.zeros((N,M),np.float32)

for u in range (0,N,1):
    for v in range (0,M,1):
        sum=0
        for m in range (0,N,1):
            for n in range (0,M,1):
                sum=sum+image[u,v]
                temp=image[m,n]*(fn.e**(-(1j*2.0*fn.pi*(u*m+v*n)/N)))
        DFT_Image[u,v]=(1/(M*N))*temp
        print(u,v,DFT_Image[u,v])

cv.imshow("DFT image",DFT_Image)

def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g

def EulerIdentity():
    #e**πi + 1 = 0   where e - Euler's number, 2.718; π - pi, 3.14159; i - imaginary number, equal to √-1 (i**2 = -1)  
    print (f"{(fn.e**(fn.pi*1j)) + 1:.12f}")
    return 0

cv.waitKey(0)
cv.destroyAllWindows()
