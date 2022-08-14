import cv2
import numpy as np

#draw with rubiks cube xd

def getColorBounds(img): #clean this up
    #do this for all colors
    colorBounds = []
    for i in range(len(colorDict)):
        color = colorHSV[i]
        mask = cv2.inRange(img, color[0:3], color[3:6])
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        x,y,w,h = 0,0,0,0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                x,y,w,h = cv2.boundingRect(approx)
        colorBounds.append((x,y,w,h))
    return colorBounds

def drawCanvas(img, myPoints):
    for i in range(len(colorDict)):
        colorPoints = myPoints[i]
        for point in colorPoints:
            x,y,w,h = point
            cv2.circle(img, (x+(w//2),y), 10,
                       colorBGR[i], cv2.FILLED)

colorDict = {"blue":0, "green":1}
colorHSV = np.array([[88,106,107,130,255,255],
                     [45,73,0,81,255,255]])
colorBGR = [(255,0,0), (0,255,0)]

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

myPoints = [[],[],[]]

draw = 0   
while True:
    succ, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgBlank = np.zeros_like(img)
    colorBounds = getColorBounds(imgHSV)

    
    for i in range(len(colorDict)): 
        boundbox = colorBounds[i]
        x,y,w,h = boundbox
        #cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 2)
        cv2.circle(imgBlank, (x+(w//2),y), 10,
                   colorBGR[i], cv2.FILLED)
        if draw and (boundbox not in myPoints[i]):
            myPoints[i].append(boundbox)

    
    drawCanvas(img, myPoints)
    cv2.imshow("Cam", np.flip(img, axis =1))


    key = cv2.waitKey(1) & 0xFF
    if key == 13:
        break
    elif key == 99:
        myPoints = [[],[],[]]
    elif key == 100:
        if draw == 0:
            draw = 1
        else:
            draw = 0
    elif key == 68:
        draw = 0


cv2.destroyAllWindows()
exit()
