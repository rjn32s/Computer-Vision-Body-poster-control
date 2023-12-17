import pyautogui
import time

# get the size of the screen
screenWidth, screenHeight = pyautogui.size()

# blink the screen 5 times
for i in range(5):
    pyautogui.click(screenWidth/2, screenHeight/2) # click on the center of the screen
    time.sleep(0.5) # wait for 0.5 seconds
    pyautogui.click(screenWidth/2, screenHeight/2) # click again on the center of the screen
    time.sleep(0.5) # wait for 0.5 seconds
