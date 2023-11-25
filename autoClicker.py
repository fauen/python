import pyautogui
import keyboard
keyboard.wait('s')
while not keyboard.is_pressed('k'):
    pyautogui.click()