import cv2
import numpy as np

def f(a):
    pass

img = cv2.imread('Resources/lambo.png')
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Trackbar window
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", (640,240))
cv2.createTrackbar("hue min", "Trackbars", 0, 179, f)
cv2.createTrackbar("hue max", "Trackbars", 179, 179, f)
cv2.createTrackbar("sat min", "Trackbars", 0, 255, f)
cv2.createTrackbar("sat max", "Trackbars", 255, 255, f)
cv2.createTrackbar("val min", "Trackbars", 0, 255, f)
cv2.createTrackbar("val max", "Trackbars", 255, 255, f)

while True:
    hmin = cv2.getTrackbarPos("hue min", "Trackbars")
    hmax = cv2.getTrackbarPos("hue max", "Trackbars")
    smin = cv2.getTrackbarPos("sat min", "Trackbars")
    smax = cv2.getTrackbarPos("sat max", "Trackbars")
    vmin = cv2.getTrackbarPos("val min", "Trackbars")
    vmax = cv2.getTrackbarPos("val max", "Trackbars")

    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])

    mask = cv2.inRange(imgHSV, lower, upper)

    imgRes = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('result', imgRes)
    
    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()
