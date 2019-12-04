
import cv2 as cv
import numpy as np

ip_image = np.array((
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]), dtype="uint8")
ip_image=(ip_image)*255

se0=np.array(([0,0,1,0,0],
             [0,0,1,0,0],
             [1,1,1,1,1],
             [0,0,1,0,0],
             [0,0,1,0,0]), dtype="uint8")
se0=se0*255

se=np.array(([0,1,0],[1,1,1],[0,1,0]),dtype="uint8")
se=se*255

dim=(512,512)

#cv.imshow("Zoomed I/p image",cv.resize(ip_image,dim,interpolation=cv.INTER_AREA))
#cv.imshow("Zoomed SE",cv.resize(se,(230,230),interpolation=cv.INTER_AREA))

w=np.uint8(np.floor(se.shape[0]/2))
h=np.uint8(np.floor(se.shape[1]/2))

Dila_image = np.zeros((7,7),np.uint8)
Eros_image = np.zeros((7,7),np.uint8)
#Open_image = np.zeros((7,7),np.uint8)
#Clos_image = np.zeros((7,7),np.uint8)

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
Dil=Dilation(ip_image,se1,Dila_image)

#cv.imshow("Zoomed Dil",cv.resize(Dil,dim,interpolation=cv.INTER_AREA))

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
Ero=Erosion(ip_image,se1,Eros_image)


'''example'''

ip_image1 = np.zeros((100,400,1),np.uint8)
op_image1 = np.zeros((100,400,1),np.uint8)

cv.putText(ip_image1,
           'text_to_show',
           (80,60), 
           fontFace=cv.FONT_HERSHEY_PLAIN, 
           fontScale=2,
           color=(255))

#cv.imshow("Text Image",ip_image1)
#op_image1=Dilation(ip_image1,se,op_image1)
#cv.imshow("op_text_image",op_image1)

ip_ex=cv.imread(r"davinci.png",0)
cv.imshow("Templet image",ip_ex)

Tot=(ip_ex.shape[0]+1)*(ip_ex.shape[1]+1)
sum=0

for x in range (ip_ex.shape[0]):
    for y in range (ip_ex.shape[1]):
        sum=sum+ip_ex[x,y]
mean=sum/Tot
    

Thr_ex=np.zeros((ip_ex.shape[0],ip_ex.shape[1],1),np.uint8)

for x in range (ip_ex.shape[0]):
    for y in range (ip_ex.shape[1]):
        if (ip_ex[x,y]<=mean):
            Thr_ex[x,y] = 0
        else:
             Thr_ex[x,y] = 255
cv.imshow("Thresholded Templet image",Thr_ex)


Inv_ex=np.zeros((ip_ex.shape[0],ip_ex.shape[1],1),np.uint8)
for p in range (Thr_ex.shape[0]):
    for q in range (Thr_ex.shape[1]):
        Inv_ex[p,q]=255-Thr_ex[p,q]
cv.imshow("Inverted Templet image",Inv_ex)        


Dil_ex=np.zeros((ip_ex.shape[0],ip_ex.shape[1],1),np.uint8)
Dil_ex=Dilation(Inv_ex,se,Dil_ex)
cv.imshow("Result of Dilation",Dil_ex)

Open_ex=np.zeros((ip_ex.shape[0],ip_ex.shape[1],1),np.uint8)
Open_ex=Erosion(Dil_ex,se,Open_ex)
cv.imshow("Result of Opening",Open_ex)

cv.waitKey(0)
cv.destroyAllWindows()
