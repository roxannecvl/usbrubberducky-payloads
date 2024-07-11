import os
try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui
import random
import time

screen_width, screen_height = pyautogui.size()
for i in range (60):
    # Generate random offsets
    if random.choice([True, False]):  # Randomly choose between True (first range) and False (second range)
        x_offset = random.randint(-500, -300)
    else:
        x_offset = random.randint(300, 500)

    if random.choice([True, False]):  # Randomly choose between True (first range) and False (second range)
        y_offset = random.randint(-400, -150)
    else:
        y_offset = random.randint(150, 400)

    # Calculate the new position relative to the current position
    new_x = pyautogui.position().x + x_offset
    new_y = pyautogui.position().y + y_offset

    # Ensure the new position stays within the screen bounds
    new_x = max(10, min(new_x, screen_width - 10))
    new_y = max(10, min(new_y, screen_height -10))

    # Move the mouse cursor to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.25)
    time.sleep(0.1)  # 1 second delay
