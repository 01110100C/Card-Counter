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
      # for loop that will keep looping until the thread is stopped. 
      # Loop grabs the frame from the active stream.
        for f in self.streamn: 
           self.frame = f.array
           self.rawCapture.truncate(0)
        if self.stopped:
               self.stream.close()
               self.rawCapture.close()
               self.camera.close()
               return
        (self.grabbed, self.frame) = self.stream.read()

# Method to return the most recent frame
def read(self):
         return self.frame 
# Method to stop the thread and camera 
def stop(self):
         self.stopped = True

    

