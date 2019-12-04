import cv2 as cv
import numpy as np

ip_ex=cv.imread(r"davinci.png",0)

w=ip_ex.shape[0]
h=ip_ex.shape[1]

omega1=np.zeros((w,h),np.uint8)
omega2=np.zeros((w,h),np.uint8)

TotPix=(w)*(h)

cv.imshow("Original image",ip_ex)

sum=0
for x in range (w):
    for y in range (h):
        sum=sum+ip_ex[x,y]
OptmlThr=sum/TotPix

def Thresholding(ip_ex,OptmlThr=0):
        mean1=mean2=0
        count1=count2=0
        for x in range (w):
            for y in range (h):
                if(ip_ex[x,y]<=OptmlThr):
                    omega1[x,y]=ip_ex[x,y]
                    mean1=mean1+omega1[x,y]
                    count1+=1
                else:
                    omega2[x,y]=ip_ex[x,y]
                    mean2=mean2+omega2[x,y]
                    count2+=1
        OptmlThr=((mean1/count1)+(mean2/count2))/2
        return OptmlThr


Thr=Thresholding(ip_ex,OptmlThr)

#while(Thr-OptmlThr==0.1):
#    Thr=Thresholding(ip_ex,Thr)
    
Thr1=Thresholding(ip_ex,Thr)
Thr2=Thresholding(ip_ex,Thr1)
Thr3=Thresholding(ip_ex,Thr2)
Thr4=Thresholding(ip_ex,Thr3)
Thr5=Thresholding(ip_ex,Thr4)
Thr6=Thresholding(ip_ex,Thr5)
Thr7=Thresholding(ip_ex,Thr6)
Thr8=Thresholding(ip_ex,Thr7)
Thr9=Thresholding(ip_ex,Thr8)
Thr10=Thresholding(ip_ex,Thr9)
Thr11=Thresholding(ip_ex,Thr10)
Thr12=Thresholding(ip_ex,Thr11)

# need help above with a recurrence

cv.imshow("omega 1 image",omega1)
cv.imshow("omega 2 image",omega2)

Thr_ex=np.zeros((ip_ex.shape[0],ip_ex.shape[1],1),np.uint8)

for x in range (ip_ex.shape[0]):
    for y in range (ip_ex.shape[1]):
        if (ip_ex[x,y]<=Thr1):
            Thr_ex[x,y] = 0
        else:
             Thr_ex[x,y] = 255
cv.imshow("Thresholded image",Thr_ex)

cv.waitKey(0)
cv.destroyAllWindows()
