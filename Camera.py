## Camera Video Stream 
## Description: This file handles the camera video stream functionality. 

from threading import Thread 
from flask import Flask, Response
from picamera2 import Picamera2
import cv2

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

# Function to generate frames from the camera stream
# Buffer compresses the raw Numpy array into a JPEG format for streaming.
# yield pauses the data send the n resumes on the next loop iteration, this is what makes 
# it a stream.

def generate_frames():
    while True:
        frame = picam2.capture_array() 
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        
@app.route('\stream')
def index():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/')
def index():
    return '<img src="/stream" width="640" height="480">'


# Starts the flask web server. this host controls who can connect to the sever. 
# 0.0.0.0 listens on all available interfaces, allowing connections from any IP address.
app.run(host='0.0.0.0', port=5000, debug=True)



    


