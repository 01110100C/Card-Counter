from threading import thread 
import cv2

class Video:
    """Camera object"""
    def __init__(self, resolution=(640,480),framerate=30,src=0):

        # Import packages from picamera library
        from picamera.array import PiRGBArray
        from picamera import PiCamera

        # Initialize the PiCamera and the camera image stream
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera,size=resolution)
        self.stream = self.camera.capture_continuous(
        self.rawCapture, format = "bgr", use_video_port = True)

        # Initialize variable to store the camera frame
        self.frame = []


	    # Create a variable to control when the camera is stopped
        self.stopped = False

    def start(self):
	# Start the thread to read frames from the video stream
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
         # Keep looping indefinitely until the thread is stopped
        for f in self.stream:
        # Grab the frame from the stream and clear the stream
        # in preparation for the next frame
            self.frame = f.array
            self.rawCapture.truncate(0)

        if self.stopped:
        # Close camera resources
            self.stream.close()
            self.rawCapture.close()
            self.camera.close()


    def read(self):
		# Return the most recent frame
        return self.frame

    def stop(self):
		# Indicate that the camera and thread should be stopped
        self.stopped = True