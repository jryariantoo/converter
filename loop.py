import pyautogui
import math
import time
import keyboard  # Import the keyboard module

center_x, center_y = 960, 540
radius = 200
speed = 1000
angle = 0

while True:
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pyautogui.moveTo(x, y, duration=0.001)
    angle += 0.05
    if angle >= 2 * math.pi:
        angle = 0

    if keyboard.is_pressed('space'):  # Check if the space key is pressed
        break  # Exit the loop if the space key is pressed

    time.sleep(0)
