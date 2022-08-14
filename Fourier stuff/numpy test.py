import numpy as np
import matplotlib.pyplot as plt
import cv2

a = np.array([[0,0.1],
             [1,3]])

#a = a/a.max()

#aScaled = cv2.resize(a, (0,0), None, 200, 200)

cv2.imshow(a)
plt.show()
