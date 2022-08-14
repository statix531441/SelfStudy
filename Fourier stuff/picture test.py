import numpy as np
import cv2
import matplotlib.pyplot as plt
import fft
import gk

img = cv2.imread('Resources/loli.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imgGray = imgGray/imgGray.max()
#imgGray -=1
imgGrayCropped = imgGray[:128,:256]

feature = np.zeros((150,70))
feature[:,:10] = 1
feature[:,10:60] = -1
feature[:,60:] = 1

feature = gk.Gkernel((7,7),1)

f = abs(fft.fft2(imgGray,imgGray.shape[1]//2,
                 imgGray.shape[0]//2))

z = (f>2500).astype('int32')




featureMap = fft.conv2(imgGray, feature)

if featureMap.min()<0:
    featureMap = featureMap - featureMap.min()
    
featureMap = featureMap/featureMap.max()


cv2.imshow('Image', imgGray)
cv2.imshow('Map', featureMap)

plt.figure()
plt.imshow(feature)
plt.figure()
plt.imshow(f)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
