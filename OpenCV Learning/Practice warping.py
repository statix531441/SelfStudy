import cv2
import numpy as np

img = cv2.imread('Resources/cards.jpg')

width, height = 400,600

pts1 = np.float32([[557,28], [817,27], [559,410], [844,414]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgRes = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow('ez', imgRes)



cv2.waitKey(0)
cv2.destroyAllWindows()
