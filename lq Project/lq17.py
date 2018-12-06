'''
色彩空间之间的颜色互换
'''
import cv2 as cv
import numpy as np
'''
def extrace_obj_demo():
    capture=cv.VideoCapture("../data/vedo1.mp4")
    while True:
        ret,frame=capture.read()
        if ret==False:
            break;
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv=np.array([37,43,46])
        upper_hsv=np.array([77,255,255])
        mask=cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c=cv.waitKey(40)
        if c==27:
            break;
'''
def color_dpace_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv= cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hav", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    Ycrcb= cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb", Ycrcb)


print("**"*20)

src=cv.imread("../data/5.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
print(src.shape)
t1=cv.getTickCount()
color_dpace_demo(src)
t2=cv.getTickCount()

time=(t2-t1)/cv.getTickFrequency()

print("time:%s ms"%(time*1000))

cv.waitKey(0)

cv.destroyAllWindows()