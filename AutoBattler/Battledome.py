import pyautogui as pag
import time
import keyboard
import random

# Constants
IMAGE_CONFIDENCE = 0.85

def locate_image_on_screen(image_path, confidence=IMAGE_CONFIDENCE):
    """
    Locate the given image on the screen and return its location.

    :return: Location of the image if found, None otherwise.
    """
    try:
        return pag.locateOnScreen(image_path, confidence=confidence)
    except Exception as e:
        print(f"Error locating image: {e}")
        return None

def move_cursor_to_center_of_location(location):
    if location:
        center_x, center_y = pag.center(location)
        pag.moveTo(center_x, center_y)

def main(found_image_locations, is_last_round):
    # List of image paths
    image_paths = [
        r"2fight.jpg",
        r"3weapon.jpg",
        r"4Machete.jpg",
        r"5weapon2.jpg",
        r"6Heal.jpg",
        r"7Ability.jpg",
        #r"8Medidate.jpg",
        r"8Icicle.jpg",
        r"2fight.jpg",
        r"9FastForward.jpg",
        r"10Collect.jpg",
        r"1playagain.jpg"
        # Add more image paths as needed
    ]
    
    
    for image_path in image_paths:
        print(f"Looking for image: {image_path}")
        
        
        # Skip clicking on the "play again" image in the last round
        if is_last_round and image_path == r"1playagain.jpg":
            print("Final round: Skipping 'play again' click.")
            continue
        
        i=0
        if image_path == r"9FastForward.jpg":
            while locate_image_on_screen(image_path) is None and i<15:
                print("Waiting for combat...")
                time.sleep(.1)  # Sleep for .5 second and try again
                i += 1
        i=0
        if image_path == r"3weapon.jpg":
            while locate_image_on_screen(r"9FastForward.jpg") is None and i < 15:
                print("Waiting for monologue...")
                time.sleep(.1)  # Sleep for .1 second and try again
                i += 1
        
        time.sleep(.01)

        if image_path not in found_image_locations:
            # If the image location is not already stored, locate the image on the screen
            location_of_image = locate_image_on_screen(image_path)
            
            if location_of_image:
                print(f"Image found: {location_of_image}")
                # Store the found location in the dictionary
                found_image_locations[image_path] = location_of_image
            else:
                print(f"Image not found on screen: {image_path}")
                continue  # Skip to the next iteration of the loop
        else:
            # If the image location is already stored, retrieve it from the dictionary
            location_of_image = found_image_locations[image_path]
            print('Using Saved Location')
            
        # Move the cursor to the center of the located image
        move_cursor_to_center_of_location(location_of_image)
        
        
        # Perform a left click
        pag.click()
        

if __name__ == "__main__":

    # Dictionary to store the locations of the found images
    found_image_locations = {}

    #Total Number of Rounds
    total_rounds = 50

    for i in range(total_rounds):
        # Check if the current round is the last one
        is_last_round = (i == total_rounds - 1)

        main(found_image_locations, is_last_round)
        print(f"Round {i + 1} completed. Moving to the next round...\n")

        # If it's the last round, don't wait for the "play again" image, break the loop
        if is_last_round:
            break

        # Check for the availability of the image
        fight_image_path = r"2fight.jpg"
        i=0
        while locate_image_on_screen(fight_image_path) is None and i < 15:
            print("Waiting for the next round...")
            time.sleep(.3)  # Sleep for .3 second and try again
            i += 1


    print("All rounds completed.")
