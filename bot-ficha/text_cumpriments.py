from datetime import datetime
from time import sleep
import pyautogui


CURRENT_TIME = datetime.now().ctime()

CURRENT_TIME = CURRENT_TIME.split()
print(CURRENT_TIME[3][0:2])

def do_cumpriment_by_time():
    sleep(1)
    hour = int(CURRENT_TIME[3][0:2])
    if hour >= 5 and hour <= 12:
        pyautogui.write('Bom dia gente !')
        return
    elif hour >= 12 and hour <= 18:
        pyautogui.write('Boa tarde gente !')
        return
    elif hour >= 18 and hour <= 00:
        pyautogui.write('Boa madru !')
        return


def do_cumpriment_showing_time():
    sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write(f'Agora são {CURRENT_TIME[3]}')
    pyautogui.press('enter')

def do_cumpriment_in_test():
    sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write('Oi :sorriso')
    pyautogui.press('enter')
    pyautogui.write("""eu sou Jason, o pastoleiro,
    estou fazendo uns testes com mensagens, espero que n se importem.""")
    pyautogui.press('enter')


if __name__ == '__main__':
    from unittest import main, TestCase

    class ModuleFunctionTestCase(TestCase):
        def test_cumpriment_msg(self):
            pyautogui.hotkey('ctrl', 'n')
            do_cumpriment_in_test()

        def test_do_cumpriment_by_time(self):
            do_cumpriment_by_time()

        def test_do_cumpriment_by_showing_time(self):
            do_cumpriment_showing_time()

    main()