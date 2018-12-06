'''
边缘保留滤波EPF
'''
import cv2 as cv
import numpy as np

def bi_demo(image):
    dst=cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi_demo",dst)

def shift_demo(image):
    dst=cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("shift_demo", dst)

print("**"*20)

src=cv.imread("../data/lvbo3.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)



t1=cv.getTickCount()
bi_demo(src)
shift_demo(src)
t2=cv.getTickCount()
time=(t2-t1)/cv.getTickFrequency()


print("time:%s ms"%(time*1000))
cv.waitKey(0)

cv.destroyAllWindows()
