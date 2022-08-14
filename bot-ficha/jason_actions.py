from unittest import TestCase, main
from writers import text_assests
from time import sleep
import pyautogui

import jason_pastoleiro

jason = jason_pastoleiro.Jason('Actions jason')

def find_whats(group_name:str):
    sleep(1)
    pyautogui.press('win')
    pyautogui.write('Whatsapp', interval=0.05)
    pyautogui.press('enter')
    sleep(17)
    pyautogui.click(x=99, y=116)
    sleep(2)
    pyautogui.write(group_name)
    sleep(0.5)
    pyautogui.click(x=133, y=268)


def do_list_of_kids(sector, group_name='Audios'):
    find_whats(group_name)
    sleep(5)
    pyautogui.click(x=608, y=688)
    jason.make_list_kids(sector)
    text_assests.close_archives()


if __name__ == '__main__':
    class TestFuctions(TestCase):
        def test_list_of_kids(self):
            list_of_kids = do_list_of_kids('clube')

    main()
