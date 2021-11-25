'''Mini Capstone Project
Raspberry Pi Motion Detector / Video Recorder / Audio Alert
By Philip Bartoo
11/10/21
Note: This code is intended to run on the Raspberry Pi'''

from gpiozero import MotionSensor
from gpiozero import Buzzer
from picamera import PiCamera
from datetime import datetime
from time import sleep
import logging

pir = MotionSensor(4,threshold=0.2)
camera = PiCamera()
camera.rotation = 180
buzzer = Buzzer(17)
logging.basicConfig(filename='/home/pi/Desktop/video.log',level=logging.INFO)

def record_log():
    log_time = datetime.now().strftime('%m-%d-%y,%H:%M:%%S')
    return log_time

while True:
    pir.wait_for_motion()
    logging.info(record_log() + ' Motion detected')
    buzzer.on()
    camera.start_recording('/home/pi/Desktop/' + record_log() + '.h264')
    logging.info(record_log() + ' Starting to record')
    pir.wait_for_no_motion()
    logging.info(record_log() + ' Motion no longer detected')
    buzzer.off()
    camera.stop_recording()
    logging.info(record_log() + ' Recording stopped')