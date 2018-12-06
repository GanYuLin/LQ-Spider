'''
像素运算
'''
import cv2 as cv
import numpy as np

# 像素加
def add_demo(m1,m2):
    dst=cv.add(m1,m2)
    cv.imshow("add_demo",dst)
# 像素减
def substract_demo(m1,m2):
    dst=cv.subtract(m1,m2)
    cv.imshow("substract_demo",dst)


# 像素乘
def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


# 像素除
def divide_demo(m1,m2):
    dst=cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)

# 像素主色调
def others(m1,m2):
    # M1=cv.mean(m1)
    # M2= cv.mean(m2)
    # print(M1)
    # print(M2)

    M1,dev1=cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    print(M1)
    print("----")
    print(dev1)
    print("----")
    print(M2)
    print("----")
    print(dev2)


def logic_demo(m1,m2):
    # 与
    # dst=cv.bitwise_and(m1,m2)
    # 或
    dst = cv.bitwise_or(m1, m2)
    cv.imshow("logic_demo", dst)

def contrast_brightness_demo(image,c,b):
    h,w,ch=image.shape
    blank=np.zeros([h,w,ch],image.dtype)
    dst=cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("con_bri_demo",dst)



print("**"*20)

src1=cv.imread("../data/linux.jpg")
src2=cv.imread("../data/win1.jpg")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
print(src1.shape)
print(src2.shape)

# cv.imshow("image1",src1)
# cv.imshow("image2",src2)

src=cv.imread("../data/5.jpg")
cv.imshow("image3",src)
t1=cv.getTickCount()
contrast_brightness_demo(src,1.2,25)
# color_dpace_demo(src)
# add_demo(src1,src2)
# substract_demo(src1,src2)
# divide_demo(src1,src2)
# multiply_demo(src1,src2)

# others(src1,src2)

# 逻辑运算
# logic_demo(src1,src2)
t2=cv.getTickCount()

time=(t2-t1)/cv.getTickFrequency()

print("time:%s ms"%(time*1000))

cv.waitKey(0)

cv.destroyAllWindows()



