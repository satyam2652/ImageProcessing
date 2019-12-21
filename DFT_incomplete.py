
import numpy as np
import cv2 as cv
import math as fn
image=np.array(([3,2],
                [2,1]), dtype="uint8")

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
        

cv.waitKey(0)
cv.destroyAllWindows()
