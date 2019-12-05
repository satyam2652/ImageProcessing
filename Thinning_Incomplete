import cv2
import numpy as np
 
# Create an image with text on it
img = np.zeros((100,400),dtype='uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'TheAILearner',(5,70), font, 2,(255),5,cv2.LINE_AA)
img1 = img.copy()
 
# Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))


ip_image1 = np.zeros((100,400,1),np.uint8)
op_image1 = np.zeros(ip_image1.shape,np.uint8)

cv2.putText(ip_image1,
           'text_to_show',
           (80,60), 
           fontFace=cv2.FONT_HERSHEY_PLAIN, 
           fontScale=2,
           color=(255))

se=np.array(([0,1,0],[1,1,1],[0,1,0]),dtype="uint8")

# Create an empty output image to hold values
thin = np.zeros(img.shape,dtype='uint8')

w=np.uint8(np.floor(se.shape[0]/2))
h=np.uint8(np.floor(se.shape[1]/2))

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

Ero=Erosion(ip_image1,se,op_image1)


# Loop until erosion leads to an empty set
while (cv2.countNonZero(ip_image1)!=0):
    # Erosion
    erode = cv2.erode(img1,kernel)
    # Opening on eroded image
    opening = cv2.morphologyEx(erode,cv2.MORPH_OPEN,kernel)
    # Subtract these two
    subset = erode - opening
    # Union of all previous sets
    thin = cv2.bitwise_or(subset,thin)
    # Set the eroded image for next iteration
    img1 = erode.copy()
    
cv2.imshow('original',img)
cv2.imshow('thinned',thin)

cv2.waitKey(0)
cv2.destroyAllWindows()
