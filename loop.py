import pyautogui
import math
import time

# Define the parameters of the circular loop
center_x, center_y = 500, 500  # Center of the circle
radius = 200  # Radius of the circle
speed = 100  # Movement speed (pixels per second)

# Calculate the initial angle
angle = 0

while True:
    # Calculate the new cursor position based on the angle
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    # Move the cursor to the new position
    pyautogui.moveTo(x, y, duration=0.1)

    # Increment the angle
    angle += 0.05  # You can adjust this value to control the speed of the loop

    # Wrap around the circle
    if angle >= 2 * math.pi:
        angle = 0

    # Pause briefly to control the loop speed
    time.sleep(0.01)
