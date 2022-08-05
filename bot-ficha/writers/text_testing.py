import pyautogui

from time import sleep

def write_end_test_msg():
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write('______________________________')
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write('Esta e uma mensagem de teste automatica, eu ainda estou aprendendo, mas finalizei esse teste !', interval=0.1)
    pyautogui.write(':sorriso ', interval=0.1)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'enter')
    sleep(1)
    pyautogui.hotkey('enter')


def inform_kids_quant(kids_quant: int):
    pyautogui.press('enter')
    pyautogui.write(f'Hoje eu vou estar fazendo um teste de mensagens com um total de {kids_quant} criancas :animado')
    pyautogui.press('enter', 2, interval=1) 