import pyautogui
from time import sleep

def make_generic_warning(msg):
    sleep(1.5)
    pyautogui.write(f'Jason >>>{msg}')
    pyautogui.press('enter')
