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

def identify_card(card_region):
    gray = cv2.cvtColor(card_region, cv2.COLOR_BGR2GRAY)
    best_match = None
    best_score = 0

    for name, template in templates.items():
         resized = cv2.resize(template, (gray.shape[1], gray.shape[0]))
         result = cv2.matchTemplate(gray, resized, cv2.TM_CCOEFF_NORMED)
         score = result.max()

         if score > best_score:
              best_score = score
              best_match = name
        
         if best_score > 0.7: 
            return best_match
         



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


        