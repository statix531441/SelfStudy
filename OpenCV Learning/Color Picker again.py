import cv2
import numpy as np

def f(a):
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("hue min","Trackbars",0,179,f)
cv2.createTrackbar("sat min","Trackbars",0,255,f)
cv2.createTrackbar("val min","Trackbars",0,255,f)
cv2.createTrackbar("hue max","Trackbars",179,179,f)
cv2.createTrackbar("sat max","Trackbars",255,255,f)
cv2.createTrackbar("val max","Trackbars",255,255,f)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    succ, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hmin=cv2.getTrackbarPos("hue min","Trackbars")
    smin=cv2.getTrackbarPos("sat min","Trackbars")
    vmin=cv2.getTrackbarPos("val min","Trackbars")
    hmax=cv2.getTrackbarPos("hue max","Trackbars")
    smax=cv2.getTrackbarPos("sat max","Trackbars")
    vmax=cv2.getTrackbarPos("val max","Trackbars")

    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])

    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("Anal sex", img)

    cv2.imshow("buttsex", mask)

    if cv2.waitKey(1) == 13:
        print(lower, upper)
    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()
