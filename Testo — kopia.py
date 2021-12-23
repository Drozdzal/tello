from djitellopy import tello
from time import sleep
import cv2
import numpy as np

def Show_img():
    img = Dron.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("image", img)
    cv2.waitKey(1)
def Get_Center_Point():
        lower = np.array([0, 114, 66])
        upper = np.array([16, 255, 255])
        img = Dron.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # do gray
        field_mask = cv2.inRange(imgHSV, lower, upper)
        field_mask = cv2.GaussianBlur(field_mask, (11, 11), 0)
        field_mask=cv2.medianBlur(field_mask,27)
        circles=cv2.HoughCircles(field_mask,cv2.HOUGH_GRADIENT,1,20,param1=200,param2=30,minRadius=0,maxRadius=0)
        try:
            detected_circles=np.uint16(np.around(circles))
            for(x,y,r) in detected_circles[0,:]:
                cv2.circle(img,(x,y),2,(0,255,255),3)
        except:
            pass
        cv2.imshow("okienkoo",field_mask)
        cv2.imshow("okienko",img)
        cv2.waitKey(1)

Dron=tello.Tello()
Dron.connect()
print(Dron.get_battery())

Dron.streamon()
s=True
while s:
    Get_Center_Point()
    #s=False
