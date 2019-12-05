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

OldThr=OptmlThr
NewThr=Thresholding(ip_ex,OptmlThr)

Thr=[]

while(abs(NewThr-OldThr) >= 0.1):
    OldThr=NewThr
    NewThr=Thresholding(ip_ex,NewThr)
    Thr.append(NewThr)
    #print("NewThr",NewThr)
    
for x in range (len(Thr)):
    print(Thr[x],end="\t")
 
cv.imshow("omega 1 image",omega1)
cv.imshow("omega 2 image",omega2)

Thr_ex=np.zeros((ip_ex.shape[0],ip_ex.shape[1],1),np.uint8)

for x in range (ip_ex.shape[0]):
    for y in range (ip_ex.shape[1]):
        if (ip_ex[x,y]<=NewThr):
            Thr_ex[x,y] = 0
        else:
             Thr_ex[x,y] = 255
cv.imshow("Thresholded image",Thr_ex)

cv.waitKey(0)
cv.destroyAllWindows()
