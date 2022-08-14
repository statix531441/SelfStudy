import cv2
import numpy as np

img = cv2.imread('Resources/cards.jpg')
cv2.imshow('cards', img)

width, height = 250, 350

pts1 = np.float32([[558,30], [815,28], [561,411], [844,414]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOut = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow('warped', imgOut)

cv2.waitKey(0)
cv2.destroyAllWindows()
