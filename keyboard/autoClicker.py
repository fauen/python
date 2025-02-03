import pyautogui
import keyboard
try:
    while True:
        print("Quit with Ctrl+C")
        keyboard.wait('s')
        while not keyboard.is_pressed('k'):
            pyautogui.click()
except KeyboardInterrupt:
    pass
