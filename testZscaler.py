import pyautogui
import time

# Pic 1
pic1 = "D:\\Dev\\Python\\Test\\Libraries\\pyautogui\\internet_security.png"
# Pic 2
pic2 = "D:\\Dev\\Python\\Test\\Libraries\\pyautogui\\internet_security2.png"
# Pic 3
pic3 = "D:\\Dev\\Python\\Test\\Libraries\\pyautogui\\turn_off.png"
# Textfield
pic4 = "D:\\Dev\\Python\\Test\\Libraries\\pyautogui\\enterreasons.png"
# Continue button
pic5 = "D:\\Dev\\Python\\Test\\Libraries\\pyautogui\\continueBtn.png"
# Sec off
pic6 = "D:\\Dev\\Python\\Test\\Libraries\\pyautogui\\internet_security_off.png"

# Optional safety
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Zscaler
progrm = "Zscaler"

def click_button(images, confidence=0.9, retries=3, delay=1):
    """
    Tries to locate and click a button using a list of images.
    
    Args:
    - images: List of image file names to search for.
    - confidence: Confidence level for image recognition (default: 0.9).
    - retries: Number of retries if image is not found (default: 3).
    - delay: Delay in seconds between retries (default: 1).
    """
    for attempt in range(retries):
        for image in images:
            try:
                button_location = pyautogui.locateOnScreen(image, confidence=confidence)
                if button_location:
                    button_center = pyautogui.center(button_location)
                    pyautogui.click(button_center)
                    print(f"Clicked on {image}")
                    return True
            except pyautogui.ImageNotFoundException as e:
                print(f"Attempt {attempt + 1}/{retries} - Image '{image}' not found: {e}")
        
        # If the image isn't found, wait and retry
        print(f"Retrying in {delay} seconds...")
        time.sleep(delay)

    print(f"Could not find any of the images: {images}")
    return False


# Function to type text into a text field
def type_into_text_field(image, text, confidence=0.9):
    # Locate the text field and click it
    text_field_location = pyautogui.locateOnScreen(image, confidence=confidence)
    if text_field_location:
        text_field_center = pyautogui.center(text_field_location)
        pyautogui.click(text_field_center)
        print(f"Clicked into text field using {image}")
        pyautogui.write(text)
    else:
        print(f"Could not find the text field image: {image}")

# Function to close the program using Alt+F4
def close_program():
    # Press Alt+F4 to close the program
    pyautogui.hotkey('alt', 'f4')
    print("Closed the program")

# Open Zscaler Client Connector (Windows + Search)
pyautogui.press('win')  # Press the Windows key
time.sleep(1)
pyautogui.write(progrm)  # Type the name of the app
pyautogui.press('enter')  # Open the app
time.sleep(3)  # Wait for the app to open



# Click on "Internet Security" using image recognition for either image
if click_button([pic1, pic2], confidence=0.9):
    time.sleep(2)  # Wait for the section to open
    try:
        if pyautogui.locateOnScreen(pic3, confidence=0.9):
            # Click on "TURN OFF" for Service Status using image recognition
            print("Internet Security is on. Click to turn it off.")
            click_button([pic3], confidence=0.9)

            # Click into the text field using 'enterreasons.png' and type 'XYZ'
            type_into_text_field(pic4, 'XYZ', confidence=0.9)

            # Click on the "Continue" button using 'continueBtn.png'
            click_button([pic5], confidence=0.9)

            # Close the program using Alt+F4
            close_program()

        # Check if it is already turned off by looking for 'InternetSec_on.png'
        elif pyautogui.locateOnScreen(pic6, confidence=0.95):
            print("Internet Security is already off. Closing the program.")
            # time.sleep(2)
            # Close the program using Alt+F4
            close_program()
    except Exception as e:
        print(f"An error occurred: {e}")
        close_program()
print("Automation completed!")
