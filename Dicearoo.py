import pyautogui
import time
import keyboard
import random

# Coordinates of a point within the browser window on the left
x, y = 93, 184  # Replace with the actual coordinates

# Move the mouse to the browser and click to focus
pyautogui.click(x, y)

i = 0
try:
    while keyboard.is_pressed('esc') == False and i < 100:

        # Press F5 to refresh
        pyautogui.press('f5')
        
        # Wait for a short moment for the confirmation dialog to appear
        time.sleep(random.uniform(0.005, 0.01))  # Random sleep time between 1.1 and 2.3 seconds
        
        # Press 'Enter' to confirm refresh
        pyautogui.press('enter')
        
        # Wait for a specified random time before the next refresh
        time.sleep(random.uniform(0.05, 0.1))  # Random sleep time between 1.1 and 2.3 seconds

        #Pause on the 20th run to ensure page load
        if i%25 == 0:
            time.sleep(2.5) 
        i += 1
        print ('run:',i)
except KeyboardInterrupt:

    print("Program terminated by user")
