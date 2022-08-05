import pyautogui

from time import sleep

def prepare_archive():
    sleep(2)
    pyautogui.hotkey('ctrl', 'n')

def close_arquive():
    sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    sleep(0.5)
    pyautogui.press('tab')
    sleep(0.5)
    pyautogui.press('enter')