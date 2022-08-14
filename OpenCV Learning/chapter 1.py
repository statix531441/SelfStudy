import cv2
import numpy as np

img = cv2.imread("Resources/loli.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
imgCropped = img[0:200, 200:500]

cv2.imshow('hi', imgResize)


##imgBlue = img.copy()
##imgBlue[:,:,1:3] = 0
##
##cv2.imshow('blueloli', imgBlue)
##cv2.imshow("loli after blue", img)
##
##imgGreen = img.copy()
##imgGreen[:,:,0] = imgGreen[:,:,2] = 0
##
##cv2.imshow('greenloli', imgGreen)
##
##imgRed = img.copy()
##imgRed[:,:,0:2] = 0
##
##
##cv2.imshow('redloli', imgRed)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

###############Video################
##import cv2
##import numpy as np
##
##frameWidth = 640
##frameHeight = 480
##
##cap = cv2.VideoCapture(0)
##cap.set(3, frameWidth)
##cap.set(4, frameHeight)
##cap.set(10, 100)
##
##while True:
##    success, img = cap.read()
##    mirrored =  np.flip(img, axis = 1)
##    cv2.imshow("Video", mirrored)
##    
##    if cv2.waitKey(1) == 32:
##        break
##cv2.destroyAllWindows()

