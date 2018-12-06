import cv2 as cv
import numpy as np

def video_demo():
    capture=cv.VideoCapture(0)
    while True:
        ret,frame=capture.read()
        frame=cv.flip(frame,1)
        cv.imshow("video",frame)
        c=cv.waitKey(50)
        if c==70:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data=np.array(image)
    print(pixel_data)





print("**"*20)

src=cv.imread("../img/1.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

get_image_info(src)
gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite("../data/result.jpg", gray)



# video_demo()

cv.waitKey(0)

cv.destroyAllWindows()