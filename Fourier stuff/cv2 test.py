import numpy as np
import matplotlib.pyplot as plt
import math
import cv2

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",(640,100))

cv2.createTrackbar("u","Trackbars",0,10,empty)
cv2.createTrackbar("v","Trackbars",0,10,empty)

N = 100
wave = np.zeros((N,N))

while True:
    u = cv2.getTrackbarPos("u","Trackbars")
    v = cv2.getTrackbarPos("v","Trackbars")
    for row in range(len(wave)):
        for col in range(len(wave[0])):
            wave[row][col] = 0.5*(1+math.sin(2*math.pi*(row*u + col*v)/N))
        
    #waveScaled = cv2.resize(wave, (0, 0), None, 2, 2)

    plt.imshow(wave)
    plt.pause(0.1)

    if cv2.waitKey(100)==13:
        break


cv2.destroyAllWindows()

