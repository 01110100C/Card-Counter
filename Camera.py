## Camera Video Stream 
## Description: This file handles the camera video stream functionality. 

from threading import Thread 
import cv2

class Video: 
    def __init__(self, resolution=(640,480), framerate=30, src=0): 
          
    # import pi camera packages
     from picamera.array import PiRGBArray
     from picamera import PiCamera

     self.camera = PiCamera()
     self.camera.resolution = resolution
     self.camera.framerate = framerate
     self.rawCapture = PiRGBArray(self.camera, size=self.resolution)
     self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port = True)

     self.frame =[]

     self.stopped = False

     def start(self):
        Thread(target=self.update,args=()).start()
        return self 
     
     def update(self):
        



    

