import webbrowser
import schedule
import pyautogui as pag
import keyboard
import random
import time

# Constants
webpage_url = 'https://www.neopets.com/amfphp/json.php/WheelService.spinWheel/3'

def task():
    time.sleep(random.uniform(1,5))
    webbrowser.open(webpage_url)
    time.sleep(random.uniform(.5,2))
    pag.hotkey('ctrl', 'w')

# Run the task for the first time immediately
task()
schedule.every(40).minutes.do(task)

if __name__ == "__main__":
    # Keep the script running
    while not keyboard.is_pressed('esc'):
        schedule.run_pending()
        time.sleep(1)