from datetime import datetime
from time import sleep
import test_tools
import pyautogui


CURRENT_TIME = datetime.now().ctime()

CURRENT_TIME = CURRENT_TIME.split()


def do_cumpriment_by_time():
    sleep(1)
    hour = int(CURRENT_TIME[3][0:2])
    if hour >= 5 and hour < 12:
        pyautogui.write('Bom dia povos !')
        return
    if hour >= 12 and hour < 18:
        pyautogui.write('Boa tarde gente !')
        return
    if hour >= 18 and hour < 24:
        pyautogui.write('Boa noite galerous !')
        return
    else:
        raise Exception(f'O horário fornecido não funcionou: {hour}')

def do_cumpriment_showing_time():
    sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write(f'Agora sao {CURRENT_TIME[3]}')
    pyautogui.press('enter')

def do_cumpriment_in_test():
    sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write('Oi :sorriso')
    pyautogui.press('enter')
    pyautogui.write("""eu sou Jason, o pastoleiro,
    estou espero que n se importem.""")
    pyautogui.press('enter')


if __name__ == '__main__':
    from unittest import main, TestCase

    class TextCumprimentsTestCase(TestCase):
        def test_cumpriment_msg(self):
            test_tools.prepare_archive()
            print('>>> iniciando teste de cumprimento')
            do_cumpriment_in_test()
            test_tools.close_arquive()

        def test_do_cumpriment_by_time(self):
            test_tools.prepare_archive()
            print('>>> iniciando teste de cumprimento por tempo')
            do_cumpriment_by_time()
            test_tools.close_arquive()

        def test_do_cumpriment_by_showing_time(self):
            test_tools.prepare_archive()
            print('>>> iniciando teste de cumprimento mostrando o horario')
            do_cumpriment_showing_time()
            test_tools.close_arquive()  



    main()