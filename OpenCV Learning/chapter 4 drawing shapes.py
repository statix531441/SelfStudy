import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img,(0, 300), (300, 300),
         (255, 0, 255), 3)



cv2.rectangle(img, (0,0), (256, 256), (255, 0, 0),cv2.FILLED)
cv2.circle(img, (128, 128), 20, (0,0,255), cv2.FILLED)
                        
cv2.putText(img, "Hi babe", (20, 20),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 150, 0), 2)

cv2.imshow('image', img)



cv2.waitKey(0)
cv2.destroyAllWindows()
