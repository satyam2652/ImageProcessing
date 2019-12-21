import numpy as np
import cv2 as cv
import math as fn

original = cv.imread(r"Lichtenstein.jpg",0)
dim=(32,32)
image3=cv.resize(original,dim,interpolation=cv.INTER_AREA)

image2 = np.array((
    [100, 100, 0, 0, 0, 0, 0],
    [0, 100, 100, 0, 0, 0, 0],
    [0, 0, 100, 100, 0, 0, 0],
    [0, 0, 0, 100, 100, 0, 0],
    [0, 0, 0, 0, 100, 100, 0],
    [0, 0, 0, 0, 0, 100, 100],
    [100, 0, 0, 0, 0, 0, 100]), dtype="uint8")

image1=np.array(([3,3],
                 [3,3]), dtype="uint8")

DFT_Image=np.zeros((N,M),np.float32)

def DFT2d(image):
    N=image.shape[0]
    M=image.shape[1]
    DFT_Image=np.zeros((N,M),np.float32)
    for u in range (0,N,1):
        for v in range (0,M,1):
            temp=0
            for m in range (0,N,1):
                for n in range (0,M,1):
                    temp=temp+image[m,n]*(fn.e**( -(1j) * (2.0) * (fn.pi) * ((u*m)/M+(v*n)/N)  ))
            DFT_Image[u,v]=(1/(M))*temp
    return DFT_Image

DFT_Image=DFT2d(image2)
cv.imshow("DFT image",DFT_Image)

cv.waitKey(0)
cv.destroyAllWindows()
