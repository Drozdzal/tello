from djitellopy import tello
from time import sleep

Dron=tello.Tello()
Dron.connect()
print(Dron.get_battery())
Dron.takeoff()
Dron.send_rc_control(0,50,0,0) #gives speed
sleep(2)
Dron.send_rc_control(0,0,0,0)
Dron.land()