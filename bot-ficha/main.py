from dataclasses import dataclass
from datetime import date
from logging import exception
from random import randint
import pyautogui
from time import sleep
from base_handlers import data_sanatizer as data_san
from base_handlers import terminal_logger as term_log
import json as jsn


@dataclass
class Kid:
    name: str = 'kid mock'
    years_old: int = 12
    check_in: date = date(2022, 12, 12)
    check_out: date = date(2022, 12, 30)
    apt: int = 120
    parents: str = 'parent mock'


class Receiver:
    """Classe que tem como a função receber a entrada dos dados, sejam eles quais forem, e com o auxilio do data_sanatizer
    ela formata os dados se necessário, podendo alterar.
    A ideia do receiver é polir os dados já existêntes, bem como escolher onde eles serão guardados"""
    def __init__(self, name: str = 'Receiver Mock') -> None:
        self.name = name
        self.kids_sector_list: dict[list] = {
            'clubinho':[],
            'kids club':[],
            'clube':[]
        }

    def receive_a_kid(self) -> dict:
        kid = {
            'nome': input('<<< Insira o nome: '),
            'idade': input('<<< Insira a idade: '),
            'check-in':[int(input('mês: ')), int(input('dia: '))],
            'check-out':[int(input('mês: ')), int(input('dia: '))],
            'apt':int(input('Insira o apartamento: ')),
            'responsavel': input('Insira o responsável: ')}
        return kid

    def add_kid_to_sector(self, kid:dict):
        try:
            if kid['idade'] <= 5 and kid['idade'] > 2:
                self.kids_sector_list['clubinho'].append(kid)
                return
            if kid['idade'] <= 8 and kid['idade'] > 6:
                self.kids_sector_list['kids club'].append(kid)
                return
            if kid['idade'] <= 13 and kid['idade'] > 9:
                self.kids_sector_list['clube'].append(kid)
                return
        except:
            exception(ValueError('Erro, a criança não foi adicionada em nenhum setor, verifique a idade.'))
            

class Writer:
    """Classe que dá os outputs e as respostas a certas operações, ele não avalia nada, apenas mostra os resultados. Ela tem uma
    certa lógica mas somente usada para fins de controlar as ações do Jason, podendo mandar msgs, construir tabelas, e controlar teclado
    mouse.
    """
    def __init__(self, name= 'Writer mock') -> None:
        self.name = name

    def make_kid_description(self, kid: dict):
        sleep(1)
        kid_msg = ((kid['nome']), str(kid['apt']), kid['responsavel'])
        sleep(1)
        for item in kid_msg:
            pyautogui.write(item, 0.1)
            pyautogui.write(' ', 0.1)
        pyautogui.hotkey('ctrl', 'enter')
        

class Jason:
    """Classe que une input, processamento, análise e output, de tudo. Ela funciona com base em composição. As duas classes que compoem essa
    são receiver e writer"""
    def __init__(self, name: str = 'Jason Mock'):
        self.name = name
        self.my_receiver: Receiver = Receiver()
        self.my_writer: Writer = Writer()

    def store_in_data(self):
        jason_objt = jsn.dumps(self.my_receiver.kids_sector_list, indent=2)
        with open('kids_data.json', 'w') as kids_db:
            kids_db.write((f'{jason_objt}'))

if __name__ == '__main__':
    import unittest


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
                'responsavel':(f'responsavel {kid}')})
        return kids


    class TestReceiver(unittest.TestCase):
        receiver = Receiver()
        def test_add_kid_in_range(self):
            kids_list = do_kids_by_range(10)
            for kid in kids_list:
                self.receiver.add_kid_to_sector(kid)
            print(self.receiver.kids_sector_list)
        
        def test_add_kid_to_sector(self):
            kid = {
                'nome':(f'Crianca mock'),
                 'idade':randint(3, 13),
                'check-in':[randint(1, 12),
                randint(1, 28)], 
                'check-out':[randint(1, 12),
                randint(1, 28)],
                'apt':randint(100, 400),
                'responsavel':(f'responsavel mock')}
            self.receiver.add_kid_to_sector(kid)
            print(self.receiver.kids_sector_list)
        
    class TestWriter(unittest.TestCase):
        my_writer = Writer()
        my_receiver = Receiver()

        def test_make_description_in_range(self):
            sleep(2)
            pyautogui.hotkey('ctrl', 'n')
            sleep(2)
            kids = do_kids_by_range(18)
            pyautogui.write('pastinha teste do clubinho', interval=0.05)
            pyautogui.hotkey('ctrl', 'enter')
            for kid in kids:
                self.my_receiver.add_kid_to_sector(kid)
            for kid in self.my_receiver.kids_sector_list['clubinho']:
                self.my_writer.make_kid_description(kid)

        def test_make_kid_description(self):
            kid = {
                'nome':(f'Crianca mock'),
                 'idade':randint(3, 13),
                'check-in':[randint(1, 12),
                randint(1, 28)], 
                'check-out':[randint(1, 12),
                randint(1, 28)],
                'apt':randint(100, 400),
                'responsavel':(f'responsavel mock')}
            pyautogui.hotkey('ctrl', 'n')
            self.my_writer.make_kid_description(kid)

    class TestJason(unittest.TestCase):
        jason = Jason()
        def test_store_in_data(self):
            kids = do_kids_by_range(20)
            for kid in kids:
                self.jason.my_receiver.add_kid_to_sector(kid)
            self.jason.store_in_data()

    unittest.main()