import cv2
import numpy as np

colorNames = ['Blue','Red','Green',
              #'Orange',
              'Yellow']

colorHSV =np.array(
            [[96,255,150,155,255,255], #blue
          [160,138,199,179,255,255], #red
          [54,255,180,85,255,255], #green
          #[0,89,123,14,255,255], #orange
          [16,98,162,57,255,255]] #yellow
        )

colorBGR =[[255,0,0],#blue
           [0,0,255],#red
           [0,255,0],#green
           #[255,0,255],#magenta
           [0,0,0]]#black

def getColorTips(img):

    tips = []
    
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(len(colorHSV)):
        colorRange = colorHSV[i]
        lower,upper = colorRange[0:3],colorRange[3:6]
        mask = cv2.inRange(imgHSV, lower, upper)
##        maskSmol = cv2.resize(mask, (200,150))
##        cv2.imshow(colorNames[i], maskSmol)
##
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        x,y,w,h=0,0,0,0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area>500:
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
                x,y,w,h = cv2.boundingRect(approx)
                cv2.rectangle(imgHSV, (x,y),(x+w,y+h),
                              colorBGR[i],2)
        
        tips.append((x+(w//2), y))
        
    #cv2.imshow('hsv',imgHSV)

    return tips

def drawOnCanvas(img, colorPoints):
    for i in range(len(colorPoints)):
        for point in colorPoints[i]:
            cv2.circle(img, point, 10,
               colorBGR[i], cv2.FILLED)

colorPoints = [[],
               [],
               [],
               []]

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

draw = False
while True:
    succ, img = cap.read()
    
    colorTips = getColorTips(img)

    for i in range(len(colorNames)):
        tip = colorTips[i]
        cv2.circle(img, tip, 10,
                   colorBGR[i], cv2.FILLED)
        if draw and (tip not in colorPoints[i]):
            colorPoints[i].append(tip)
            
    drawOnCanvas(img, colorPoints)
    cv2.imshow('Video', np.flip(img, axis=1))

    key = cv2.waitKey(1)
    if key == 13:
        break
    elif key == 100:
        draw = not draw
    
    elif key == 99:
        colorPoints = [[],
               [],
               [],
               []]

cv2.destroyAllWindows()
exit()
