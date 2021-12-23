import cv2
import numpy as np
from time import sleep

img = cv2.imread('obraz.jpg')
lower = np.array([0, 114, 66])
upper = np.array([16, 255, 255])
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # do gray
field_mask = cv2.inRange(imgHSV, lower, upper)
field_mask = cv2.GaussianBlur(field_mask, (11, 11), 0)
field_mask=cv2.medianBlur(field_mask,27)
circles=cv2.HoughCircles(field_mask,cv2.HOUGH_GRADIENT,1,20,param1=200,param2=30,minRadius=0,maxRadius=0)

try:
    detected_circles=np.uint16(np.around(circles))
    for(x,y,r) in detected_circles[0,:]:
        cv2.circle(img,(x,y),2,(0,255,255),3)
    print(circles)
    cv2.imshow("czysty", img)
    cv2.imshow("field_mask", field_mask)
    cv2.waitKey()
except:
    print("no kruci nie ma kolek")

def How2Move(circle_pos):
    lr, fb, ud, yr = 0, 0, 0, 0
    x,y=circle_pos
    if(x>180):
        lr=50
    elif(x<180):
        lr=-50
    if (y > 120):
        ud = 50
    elif (y < 120):
        ud= -50
    return lr, fb, ud, yr
