import pyautogui
import time
import keyboard
import random

# Coordinates of a point within the browser window on the left
x, y = 93, 184  # Replace with the actual coordinates

try:
    while True:
        if keyboard.is_pressed('esc'):  # Check if 'Esc' key is pressed
            print("Esc key pressed. Exiting...")
            break

        # Get the current mouse position
        original_position = pyautogui.position()
        
        # Move the mouse to the browser and click to focus
        pyautogui.click(x, y)
            
        # Press F5 to refresh
        pyautogui.press('f5')
        
        # Wait for a short moment for the confirmation dialog to appear
        time.sleep(random.uniform(0.08, 0.09))  # Random sleep time between 1.1 and 2.3 seconds
        
        # Press 'Enter' to confirm refresh
        pyautogui.press('enter')

        # Return the mouse to its original position
        pyautogui.moveTo(*original_position)
        
        # Wait for a specified random time before the next refresh
        time.sleep(random.uniform(0.02, 0.05))  # Random sleep time between 1.1 and 2.3 seconds

except KeyboardInterrupt:
    print("Program terminated by user")
