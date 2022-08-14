import cv2
import numpy as np

def f(a):
    pass

cv2.namedWindow('sliders')
cv2.resizeWindow('sliders',640,480)







img = cv2.imread('Resources/test.png')


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgInv = imgGray.max()+imgGray.min()-imgGray
cv2.createTrackbar('min','sliders',0,imgInv.max(),f)
cv2.createTrackbar('max','sliders',imgInv.max(),imgInv.max(),f)

while True:
    i = np.copy(imgInv)
    minD = cv2.getTrackbarPos('min','sliders')
    maxD = cv2.getTrackbarPos('max','sliders')
    i[imgInv<minD] = 0
    i[imgInv>maxD] = 0

    i = i-i.min()
    i = i/i.max()

    cv2.imshow('test', i)

    key = cv2.waitKey(32) & 0xFF
    if key == 32:
        print(key)
        break
    

# c is 99
# d is 100
# enter is 13
# space is 32
