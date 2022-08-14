import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt, True)
            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 5)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContour,(x,y),(x+w,y+h), (0,255,0), 3)

            if corners == 3: objtype = "Triangle"
            elif corners == 4:
                ar = w/float(h)
                if(ar > 0.095 and ar < 1.05): objtype = "Square"
                else: objtype = "Rectangle"
            elif corners > 7: objtype = "Circle"
            else: objtype = "None"

            cv2.putText(imgContour, objtype,
                        (x+(w//2)-30, y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (0,0,0), 2)


img = cv2.imread('Resources/shapes.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

imgBlank = np.zeros_like(img)
imgBlank[:,:] = 255,255,255

imgContour = img.copy()
getContours(imgCanny)

imgStack = stackImages(0.6, ([img, imgGray, imgBlur],
                             [imgCanny, imgContour, imgBlank]))
cv2.imshow('Stack', imgStack)


cv2.waitKey(0)
cv2.destroyAllWindows()























