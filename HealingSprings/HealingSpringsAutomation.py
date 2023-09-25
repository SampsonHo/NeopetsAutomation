import webbrowser
import schedule
import time
import pyautogui as pag
import datetime

# URL of the webpage to open
webpage_url = 'https://www.neopets.com/faerieland/springs.phtml'

# Path to the image file to locate
image_path_heal_my_pets = r'HealMyPets.jpg'
image_path_healing_potion = r'HealingPotionXX.jpg'

# Confidence level for image matching
IMAGE_CONFIDENCE = 0.85

def locate_and_right_click_image(image_path):
    try:
        pag.press('end')
        i=0
        while locate_image_on_screen(image_path) is None and i < 3:
            pag.hotkey('ctrl', 'w')
            print("Reopening webpage...")
            webbrowser.open(webpage_url)
            time.sleep(8)
            pag.press('end')
            i += 1
        
        location = pag.locateOnScreen(image_path, confidence=IMAGE_CONFIDENCE)
        if location:
            center_x, center_y = pag.center(location)
            pag.moveTo(center_x, center_y)
            pag.rightClick()
            time.sleep(1)
            open_image_in_new_tab()
            time.sleep(2)
            print('Purchase made: ', datetime.datetime.now().strftime("%H:%M:%S"))
        else:
            print(f"Image {image_path} not found on screen")
            return None
    except Exception as e:
        print(f"Error locating and right-clicking image: {e}")

def open_image_in_new_tab():
    # Navigate to 'Open link in new tab' option and press 'Enter'
    pag.press('down', presses=1)  # Adjust the number of presses as per your browser's context menu
    pag.press('enter')
    pag.hotkey('ctrl', 'tab')
    pag.hotkey('ctrl', 'w')
    

def locate_image_on_screen(image_path, confidence=IMAGE_CONFIDENCE):
    """
    Locate the given image on the screen and return its location.

    :param image_path: Path to the image file to locate.
    :param confidence: Confidence level for image matching.
    :return: Location of the image if found, None otherwise.
    """
    try:
        return pag.locateOnScreen(image_path, confidence=confidence)
    except Exception as e:
        print(f"Error locating image: {e}")
        return None


def locate_and_click_image(image_path):
    """
    Locate the given image on the screen and click it.

    :param image_path: Path to the image file to locate.
    """
    try:
        # Locate the image on the screen
        location = pag.locateOnScreen(image_path, confidence=IMAGE_CONFIDENCE)
        if location:
            # Move the cursor to the center of the located image
            center_x, center_y = pag.center(location)
            pag.moveTo(center_x, center_y)
            
            # Perform a left click
            pag.click()
            time.sleep(5)
            pag.hotkey('ctrl', 'w')

        else:
            print(f"Image {image_path} not found on screen")
    except Exception as e:
        print(f"Error locating and clicking image: {e}")

    


def task():
    webbrowser.open(webpage_url)
    time.sleep(8)
    pag.press('end')
    locate_and_right_click_image(image_path_healing_potion)
    locate_and_click_image(image_path_heal_my_pets)

# Run the task for the first time immediately
task()

# Schedule the task every 30 minutes
schedule.every(30).minutes.do(task)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
