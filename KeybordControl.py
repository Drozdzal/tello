from djitellopy import tello
from time import sleep
import Dronik_na_strzaleczkach as kp
import cv2
import numpy as np
kp.odpal()
Dron=tello.Tello()
Dron.connect()
print(Dron.get_battery())
Dron.streamon()
def getKeyboardInput():
    lr,fb,ud,yr=0,0,0,0
    speed=50
    if kp.getKey("LEFT"):
        lr=-speed
    elif kp.getKey("RIGHT"):
        lr=speed

    if kp.getKey("UP"):
        fb=speed
    elif kp.getKey("DOWN"):
        fb=-speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yr = speed
    elif kp.getKey("d"):
        yr = -speed

    if kp.getKey("q"):
        Dron.land()
    if kp.getKey("e"):
        Dron.takeoff()

    return [lr,fb,ud,yr]

lower = np.array([0, 114, 66])
upper = np.array([16, 255, 255])
while True:
    vals=getKeyboardInput()
    Dron.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    print(kp.main())
    img = Dron.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    '''
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgHSV = cv2.medianBlur(imgHSV, 17)
    field_mask = cv2.inRange(imgHSV, lower, upper)
    field_mask = cv2.GaussianBlur(field_mask, (11, 11), 0)
    field_mask = cv2.medianBlur(field_mask, 27)
    circles = cv2.HoughCircles(field_mask, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=50, maxRadius=0)
    detected_circles = np.uint16(np.around(circles))
    for (x, y, r) in detected_circles[0, :]:
        cv2.circle(img, (x, y), 2, (0, 255, 255), 3)
    cv2.imshow("okno", img)
    '''
