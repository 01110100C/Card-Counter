import numpy as np 
import time 
import Camera 

## Initialize camera settings 
IM_WIDTH = 1280
IM_HEIGHT = 720
FRAME_RATE = 30
## Add sleep to allow camera to warm up 
Camera = Camera.Video(resolution=(IM_WIDTH,IM_HEIGHT), framerate=FRAME_RATE).start()
time.sleep(2)





## create a loop that obtains frames from the camera video stream

## create a function to take the isolated card value and add it to a running count 
## accordingly. 

if(card == 2 or card == 3 or card == 4 or card == 5 or card == 6):
    count += 1
elif(card == 7 or card == 8 or card == 9):
    count += 0
elif(card == 10 or card == 'Jack' or card == 'Queen' or card
    == 'King' or card == 'Ace'):
        count -= 1
        

## Card value 2-6 are +1 count 
## Card value 7-9 are 0 count
## Card value 10-Ace are -1 count


        