'''
直方图
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def equalHist_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst=cv.equalizeHist(gray)
    cv.imshow("equalHist_demo",dst)

def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe= cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst=clahe.apply(gray)
    cv.imshow("clahe_demo", dst)

# 图形比较
def create_rgb_hist(image):
    h,w,c=image.shape
    rgbHist=np.zeros([16*16*16,1],np.float32)
    bsize=256/16
    for row in range(h):
        for col in range(w):
            b=image[row,col,0]
            g=image[row,col,1]
            r=image[row,col,2]
            index=np.int(b/bsize)*16*16+np.int(b/bsize)*16+np.int(r/bsize)
            rgbHist[np.int(index),0]=rgbHist[np.int(index),0]+1
        return rgbHist

# 巴氏距离 相关性  卡方
def hist_compare(image1,image2):
    hist1=create_rgb_hist(image1)
    hist2=create_rgb_hist(image2)

    match1=cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)

    print("巴氏距离:%s,相关性:%s,kafan:%s"%(match1,match2,match3))






print("**"*20)

# src=cv.imread("../data/lvbo4.jpg")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",src)


# equalHist_demo(src)
# clahe_demo(src)

src1=cv.imread("../data/lvbo1.jpg")
src2=cv.imread("../data/lvbo2.jpg")
cv.imshow("input image1",src1)
cv.imshow("input image2",src2)

t1=cv.getTickCount()
hist_compare(src1,src2)
t2=cv.getTickCount()
time=(t2-t1)/cv.getTickFrequency()


print("time:%s ms"%(time*1000))
cv.waitKey(0)

cv.destroyAllWindows()
