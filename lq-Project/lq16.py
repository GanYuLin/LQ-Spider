import cv2 as cv
import numpy as np



def access_picels(image):
    print(image.shape)
    height=image.shape[0]
    width=image.shape[1]
    channels=image.shape[2]
    print("width:%s;height:%s;channels:%s"%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv=image[row,col,c]
                image[row,col,c]=255-pv
    cv.imshow("pixels_demo",image)

def inverse(image):
    dat=cv.bitwise_not(image)
    cv.imshow("inverse image",dat)


def create_image():
    # 多通道
    # img=np.zeros([400,400,3],np.uint8)
    # 蓝色
    # img[:,:,0]=np.ones([400,400])*255
    # 绿色
    # img[:,:,1]=np.ones([400,400])*255
    # 红色
    # img[:,:,2]=np.ones([400,400])*255

    # 单通道
    # 初始化一张图片
    # img=np.zeros([400,400,1],np.uint8)
    # # 赋值 灰度
    # # img[:,:,0]=np.ones([400,400])*127
    # img=img*0
    # cv.imshow("now image",img)
    # cv.imwrite("../data/result1.jpg",img)

    # 填充
    m1=np.ones([3,3],np.float32)
    m1.fill(122.388)
    print(m1)

    m2=m1.reshape([1,9])
    print(m2)

    m3=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int32)
    m3.fill(3)
    print(m3)

print("**"*20)

src=cv.imread("../data/5.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

t1=cv.getTickCount()
# access_picels(src)
create_image()
# 取反
# inverse(src)

t2=cv.getTickCount()

time=(t2-t1)/cv.getTickFrequency()

print("time:%s ms"%(time*1000))
# gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
# cv.imwrite("../data/result.jpg", gray)
cv.waitKey(0)

cv.destroyAllWindows()