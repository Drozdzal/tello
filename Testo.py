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
        imgHSV = cv2.medianBlur(imgHSV, 17)
        field_mask = cv2.inRange(imgHSV, lower, upper)
        field_mask = cv2.GaussianBlur(field_mask, (11, 11), 0)
        field_mask=cv2.medianBlur(field_mask,27)
        circles=cv2.HoughCircles(field_mask,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=0,maxRadius=0)
        try:
            detected_circles=np.uint16(np.around(circles))
            for(x,y,r) in detected_circles[0,:]:
                cv2.circle(img,(x,y),2,(0,255,255),3)
            return circles
        except:
            return [180,120]
def How2Move(circle_pos=[180,120]):
    lr, fb, ud, yr = 0, 0, 0, 0
    x,y=circle_pos
    if(x>180):
        lr=-50
    elif(x<180):
        lr=50
    if (y > 120):
        ud = -50
    elif (y < 120):
        ud= 50
    print(lr, fb, ud, yr)
    return lr, fb, ud, yr
Dron=tello.Tello()
Dron.connect()
print(Dron.get_battery())

Dron.streamon()
s=True
Dron.takeoff()
s=True
i=0
while s:
    Show_img()
    Dron.send_rc_control(0, 0, 0, 0)
    try:
        circle=Get_Center_Point()
        print(circle)
        for i in circle:
            MotorVal=How2Move([i[:,0],i[:,1]])
            print(MotorVal)
            Dron.send_rc_control(0, MotorVal[1], MotorVal[2], MotorVal[3])
        sleep(0.01)
    except:
        Dron.send_rc_control(0, 0, 0, 0)
    i+=1
    #s=False
