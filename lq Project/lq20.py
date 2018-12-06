'''
模糊操作
'''
import cv2 as cv
import numpy as np

# 模糊
def blur_demo(image):
    dst=cv.blur(image,(1,5))
    cv.imshow("blur_demo",dst)

# 降噪
def median_blur_demo(image):
    dst=cv.medianBlur(image,5)
    cv.imshow("median_blur_demo",dst)

def custom_blur_demo(image):

    # kernel=np.ones([5,5],np.float32)/25

    # kernel=np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)
    # 锐化 增强立体感 总和为一  边缘梯度模糊 总和为0
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)

    dst=cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("custom_blur_demo",dst)

print("**"*20)

src=cv.imread("../data/lvbo5.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)


t1=cv.getTickCount()

# blur_demo(src)

median_blur_demo(src)
# custom_blur_demo(src)

t2=cv.getTickCount()


time=(t2-t1)/cv.getTickFrequency()

print("time:%s ms"%(time*1000))
cv.waitKey(0)

cv.destroyAllWindows()
