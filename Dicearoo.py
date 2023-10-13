'''For Dicearoo, refresh specified times. 
Must be run after first round of manual refreshes

Future Updates:
-Open Dicearoo page to eliminate manual navigation
-Create process for getting through first round of manual refreshes
-Add checks for when page refresh fails (possibly during the 25th runs)
-Add manual multiplier for sleeps to account for slower connections
'''

import pyautogui
import time
import keyboard
import random


total_refreshes = int(input("enter total refreshes: "))

# Coordinates of a point within the browser window on the left
x, y = 93, 184  # Replace with the actual coordinates

# Move the mouse to the browser and click to focus
pyautogui.click(x, y)

i = 0
try:
    while keyboard.is_pressed('esc') == False and i < total_refreshes:

        #Pause on the 20th run to ensure page load
        if i%25 == 0:
            time.sleep(random.uniform(3,7))
            print ('run:',i) 
        i += 1

        # Press F5 to refresh
        pyautogui.press('f5')
        
        # Wait for a short moment for the confirmation dialog to appear
        time.sleep(random.uniform(0.005, 0.01))  # Random sleep time between 1.1 and 2.3 seconds
        
        # Press 'Enter' to confirm refresh
        pyautogui.press('enter')
        
        # Wait for a specified random time before the next refresh
        time.sleep(random.uniform(0.5, 1.5))  # Random sleep time between 1.1 and 2.3 seconds


except KeyboardInterrupt:

    print("Program terminated by user")
