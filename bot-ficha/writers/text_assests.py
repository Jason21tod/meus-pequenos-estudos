import pyautogui
from time import sleep


def close_archives():
    sleep(1.5)
    pyautogui.hotkey('alt', 'F4')
    sleep(3.5)

