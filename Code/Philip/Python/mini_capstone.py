'''Mini Capstone Project
Raspberry Pi Motion Detector / Video Recorder / Audio Alert
By Philip Bartoo
11/10/21
Note: This code is intended to run on the Raspberry Pi'''
#import the MotionSensor module from the GPIO Zero library to operate the motion sensor
from gpiozero import MotionSensor 
#Import the Buzzer module from the GPIO Zero library to turn the buzzer on and off
from gpiozero import Buzzer
#Import the PiCamera module from the PiCamera library to operate the camera
from picamera import PiCamera
#Import the datetime module from the datetime library to be able to timestamp filenames
from datetime import datetime
#Import the logging library to enable diagnostics or for future features such as notifications
import logging

#Initiate the MotionSensor by passing it the GPIO pin number (required) and sensitivity 
#threshold value for the sensor (optional).
pir = MotionSensor(4,threshold=0.2)
#Initiate the camera through the PiCamera class
camera = PiCamera()
#Rotate the camera picture 180 degrees
camera.rotation = 180
#Initiate the Buzzer by passing the GPIO pin number (required)
buzzer = Buzzer(17)
#Establish the filename and location for the log and set the level of information we will
#capture in the log. Note that we will keep a running log of all runs.
logging.basicConfig(filename='/home/pi/Desktop/video.log',level=logging.INFO)

#Create a function to get the datetime stamp for use in the video filename and logging
def record_log():
#Capture the now datetime and display as MM-DD-YYYY, Hr:Min:Sec
    log_time = datetime.now().strftime('%m-%d-%y,%H:%M:%S')
    return log_time

#Create an infinite while loop that senses motion, turns on the camera and buzzer,
#records and logs the motion, and stops when motion stops
while True:
#Tell the motion sensor to pause until motion is sensed 
    pir.wait_for_motion()
#Once motion is sensed, log that motion is detected with the datetime. Note that the logging
#library does have a built in function for this as well
    logging.info(record_log() + ' Motion detected')
#Turn on the buzzer when motion is sensed
    buzzer.on()
#Turn on the camera and begin recording. As part of the method it is passed the location to
#store recorded video with a datetime stamp and affixing the .h264 extension
    camera.start_recording('/home/pi/Desktop/' + record_log() + '.h264')
#Log when the camera has begun recording
    logging.info(record_log() + ' Starting to record')
#The loop pauses until no motion is sensed
    pir.wait_for_no_motion()
#Log that motion is no longer sensed
    logging.info(record_log() + ' Motion no longer detected')
#Turn off the buzzer
    buzzer.off()
#Stop the camera recording
    camera.stop_recording()
#Log that the recording has stopped
    logging.info(record_log() + ' Recording stopped')

'''How the passive infared sensor (PIR) works. When the sensor detects a change in heat energy
it outputs a 5V signal for a specified amount of time (in this example set at about 1 minute).
The 5V signal is read by the Raspberry Pi as a HIGH signal.  When the specified amount of time
expires and no motion is sensed (the Raspberry Pi receives a LOW, or 0V, signal), the PIR turns off.'''