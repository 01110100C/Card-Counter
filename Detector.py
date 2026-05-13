import cv2
import numpy as np
import os 

# insert in card templates 
# name them accordingly to card ex: 2_of_hearts
templates = {}

for filename in os.listdir('card_templates/'):
     name = filename.replace('.jpg', '')
     img = cv2.imread(f'card_templates/{filename}', 0)
     templates[name] = img





# loop to keep track of running count
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


        