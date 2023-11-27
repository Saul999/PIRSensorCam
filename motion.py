#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
from datetime import datetime

camera = PiCamera()

pir = MotionSensor(4)

camera.rotation = 180
def gettime():
	time = datetime.now()
	current_time = time.strftime("%H:%M:%S")
	print(current_time)

def capturevid():
	camera.start_preview()
	camera.start_recording('/home/picam/motion_camera/CaughtOnCam.h264')
	camera.wait_recording(10)
	camera.stop_recording()
	camera.stop_preview()
	


while True:
	pir.wait_for_motion()
	print("Motion Detected at:")
	gettime()
	capturevid()
	sleep(2)
	pir.wait_for_no_motion()

	print("Motion Stopped at:")
	gettime()
	break

	
