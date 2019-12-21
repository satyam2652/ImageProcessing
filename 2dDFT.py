# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:14:55 2019

@author: student
"""

import numpy as np
import cv2 as cv
import math as fn

image=np.array(([2,3],
                [4,1]), dtype="uint8")

N=image.shape[0]
M=image.shape[1]
DFT_Image=np.zeros((N,M),np.float32)

for u in range (0,N,1):
    for v in range (0,M,1):
        temp=0
        for m in range (0,N,1):
            for n in range (0,M,1):
                temp=temp+image[m,n]*(fn.e**( -(1j) * (2.0) * (fn.pi) * ((u*m)/M+(v*n)/N)  ))
        print(temp.real,temp.imag)
        DFT_Image[u,v]=(1/(M))*temp
        print(u,v,DFT_Image[u,v])

cv.imshow("DFT image",DFT_Image)

cv.waitKey(0)
cv.destroyAllWindows()
