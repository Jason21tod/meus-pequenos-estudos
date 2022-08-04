#pasta de teste de integração, testes manuais serão feitos aqui
from main_tests import *
from unittest import TestCase, main
from text_cumpriments import *

pyautogui.FAILSAFE = 1.5

def do_pattern_msg():
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write('______________________________')
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.write('Esta e uma mensagem de teste automatica, eu ainda estou aprendendo, mas finalizei esse teste !', interval=0.1)
    pyautogui.write(':sorriso ', interval=0.1)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'enter')
    sleep(1)
    pyautogui.hotkey('enter')
    

def do_kids_by_range(kids_number):
    kids = list()
    for kid in range(0, kids_number):
        kids.append(
            {'nome':(f'Crianca {kid}'),
                'idade':randint(3, 13),
            'check-in':[randint(1, 12),
            randint(1, 28)], 
            'check-out':[randint(1, 12),
            randint(1, 28)],
            'apt':randint(100, 400),
            'responsavel':(f'responsavel{kid}')})
    return kids


class TestSuite(TestCase):
    jason_mock = Jason()
    def do_pre_description(self, kids_quant):
        do_cumpriment_showing_time()
        do_cumpriment_by_time()
        do_cumpriment_in_test()
        pyautogui.press('enter')
        pyautogui.write(f'Hoje eu vou estar fazendo um teste de mensagens com um total de {kids_quant} criancas :animado')
        pyautogui.press('enter', 2, interval=1)

    def test_add_kid_in_range(self):
        kids_list = do_kids_by_range(10)
        for kid in kids_list:
            self.receiver.add_kid_to_sector(kid)
        print(self.receiver.kids_sector_list)

    def test_kids_add(self):
        kids_list = do_kids_by_range(50)
        pyautogui.hotkey('alt', 'tab')
        pyautogui.click(duration= 1, x=472, y=250)
        sleep(2)
        pyautogui.click(duration=0.7, x=786, y=695)
        sleep(2)
        for kid in kids_list:
            self.jason_mock.my_receiver.add_kid_to_sector(kid)
    
    def test_save_at_data_base(self):
        self.jason_mock.store_in_data()
    
    def test_write_msg(self):
        sleep(3)
        self.do_pre_description(50)
        pyautogui.write('*pastinha teste do clubinho*', interval=0.1)
        pyautogui.hotkey('ctrl', 'enter')
        for kid in self.jason_mock.my_receiver.kids_sector_list['clubinho']:
            self.jason_mock.my_writer.make_kid_description(kid)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl', 'enter')
        pyautogui.write('*pastinha teste do kids club*', interval=0.1)
        pyautogui.hotkey('ctrl', 'enter')
        for kid in self.jason_mock.my_receiver.kids_sector_list['kids club']:
            self.jason_mock.my_writer.make_kid_description(kid)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl', 'enter')
        pyautogui.write('*pastinha teste do clube*', interval=0.1)
        pyautogui.hotkey('ctrl', 'enter')
        for kid in self.jason_mock.my_receiver.kids_sector_list['clube']:
            self.jason_mock.my_writer.make_kid_description(kid)
        pyautogui.hotkey('enter')
        do_pattern_msg()

main()
