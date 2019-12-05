import cv2 as cv
import numpy as np

se=np.array(([0,1,0],[1,1,1],[0,1,0]),dtype="uint8")
se=se*255

'''Find the dimensions w.r.t. center'''
w=np.uint8(np.floor(se.shape[0]/2))
h=np.uint8(np.floor(se.shape[1]/2))

se1 = np.zeros((se.shape[0],se.shape[1]),np.uint8)

''' to center the structuring element to (0,0)'''
for s in range(0-w,1+w,1):
    for t in range(0-h,1+h,1):
        se1[s,t]=se[s+w,t+h]

def Dilation(ip_image,se,Dila_image):
    for i in range(w,ip_image.shape[0]-w):
        for j in range(h,ip_image.shape[1]-h):
            Dila_image[i,j]=0
            for s in range(0-w,1+w,1):
                for t in range(0-h,1+h,1):
                    if se[s,t]==255 and ip_image[i+s,j+t]==255:
                       Dila_image[i,j]=255
                       exit
                if Dila_image[i,j]==255:
                   exit
    return Dila_image

def Erosion(ip_image,se,Eros_image):
    for i in range(w,ip_image.shape[0]-w):
        for j in range(h,ip_image.shape[1]-h):
            Eros_image[i,j]=255
            for s in range(0-w,1+w,1):
                for t in range(0-h,1+h,1):
                    if se[s,t]==255 and ip_image[i+s,j+t]==0:
                        Eros_image[i,j]=0
                        exit
                if Eros_image[i,j]==0:
                   exit
    return Eros_image

ip_ex=cv.imread(r"C:\Users\Exam\Desktop\Templet.jpg",0)
#cv.imshow("Templet image",ip_ex)

'''Mean Thresholding'''
Tot=(ip_ex.shape[0]+1)*(ip_ex.shape[1]+1)
sum=0
for x in range (ip_ex.shape[0]):
    for y in range (ip_ex.shape[1]):
        sum=sum+ip_ex[x,y]
mean=sum/Tot
Thr_ex=np.zeros(ip_ex.shape,np.uint8)
for x in range (ip_ex.shape[0]):
    for y in range (ip_ex.shape[1]):
        if (ip_ex[x,y]<=mean):
            Thr_ex[x,y] = 0
        else:
             Thr_ex[x,y] = 255
#cv.imshow("Thresholded Binary image",Thr_ex)
             
'''inverting image'''
Inv_ex=np.zeros((ip_ex.shape[0],ip_ex.shape[1],1),np.uint8)
for p in range (Thr_ex.shape[0]):
    for q in range (Thr_ex.shape[1]):
        Inv_ex[p,q]=255-Thr_ex[p,q]
cv.imshow("Binary image",Inv_ex)        

Eros_image = np.zeros(ip_ex.shape,np.uint8)
Dil_image = np.zeros(ip_ex.shape,np.uint8)
skel = np.zeros(Inv_ex.shape,np.uint8)

eroded = Erosion(Inv_ex,se1,Eros_image)
temp = cv.subtract(Inv_ex,eroded)
skel = cv.bitwise_or(skel,temp)
 
cv.imshow("Binary skeleton",skel)

cv.waitKey(0)
cv.destroyAllWindows()
