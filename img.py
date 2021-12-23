from djitellopy import tello
from time import sleep
import cv2

Dron=tello.Tello()
Dron.connect()
print(Dron.get_battery())

Dron.streamon()
s=True
while s:
    img=Dron.get_frame_read().frame
    img=cv2.resize(img,(360,240))
    cv2.imshow("image",img)
    cv2.imwrite('obraz.jpg',img)
    cv2.waitKey(1)
    s=False
