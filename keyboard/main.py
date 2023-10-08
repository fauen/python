import pyautogui
import keyboard

# Get keyboard input to then set your key
# record = keyboard.record(until='esc')
# print(record)

counter = 0

def createScreenshot():
    global counter
    filename = "screenshot-" + str(counter) + ".png"
    pyautogui.screenshot(filename)
    counter = counter + 1

keyboard.add_hotkey("prntscrn", createScreenshot)
keyboard.wait()