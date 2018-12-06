'''
直方图
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])         #numpy的ravel函数功能是将多维数组降为一维数组
    plt.show()

def image_hist(image):     #画三通道图像的直方图
    color = ('b', 'g', 'r')   #这里画笔颜色的值可以为大写或小写或只写首字母或大小写混合
    for i , color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])  #计算直方图
        plt.plot(hist, color)
        plt.xlim([0, 256])
    plt.show()

print("**"*20)

src=cv.imread("../data/3.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

t1=cv.getTickCount()
plot_demo(src)
image_hist(src)
t2=cv.getTickCount()
time=(t2-t1)/cv.getTickFrequency()


print("time:%s ms"%(time*1000))
cv.waitKey(0)

cv.destroyAllWindows()
