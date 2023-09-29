import webbrowser
import schedule
import time
import pyautogui as pag
import keyboard
import random
import datetime

# Constants
webpage_url = 'https://www.neopets.com/faerieland/springs.phtml'
image_path_heal_my_pets = r'HealMyPets.jpg'
image_path_healing_potion = r'HealingPotionXX.jpg'
IMAGE_CONFIDENCE = 0.85

def locate_image_on_screen(image_path, confidence=IMAGE_CONFIDENCE):
    try:
        return pag.locateOnScreen(image_path, confidence=confidence)
    except Exception as e:
        print(f"Error locating image: {e}")
        return None

def open_image_in_new_tab():
    # Navigate to 'Open link in new tab' option and press 'Enter'
    pag.press('down', presses=1)  # Adjust the number of presses as per your browser's context menu
    pag.press('enter')
    pag.hotkey('ctrl', 'tab')
    pag.hotkey('ctrl', 'w')

def click_image(location, right_click=False):
    center_x, center_y = pag.center(location)
    pag.moveTo(center_x, center_y)
    if right_click:
        pag.rightClick()
        time.sleep(.5)
        open_image_in_new_tab()
        print('Potion Purchase made: ', datetime.datetime.now().strftime("%H:%M:%S"))
    else:
        pag.click()
        time.sleep(.5)
        pag.hotkey('ctrl', 'w')


def locate_and_click_image(image_path, right_click=False):
    try:
        pag.press('end')
        location = None
        attempts = 0
        while location is None and attempts < 3:
            if attempts > 0:
                pag.hotkey('ctrl', 'w')
                print(f"Reopening webpage... attempt {attempts}")
                webbrowser.open(webpage_url)
                time.sleep(7)
                pag.press('end')
            location = locate_image_on_screen(image_path)
            attempts += 1
        
        if location:
            click_image(location, right_click)
        else:
            print(f"Image {image_path} not found on screen")
            pag.hotkey('ctrl', 'w')
    except Exception as e:
        print(f"Error locating and clicking image: {e}")
    


def task():
    webbrowser.open(webpage_url)
    time.sleep(random.uniform(7,9))
    locate_and_click_image(image_path_healing_potion, right_click=True)
    locate_and_click_image(image_path_heal_my_pets)


# Run the task for the first time immediately
task()
schedule.every(30).minutes.do(task)

if __name__ == "__main__":
    # Keep the script running
    while not keyboard.is_pressed('esc'):
        schedule.run_pending()
        time.sleep(1)