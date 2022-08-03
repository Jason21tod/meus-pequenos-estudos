from dataclasses import dataclass
from datetime import date
from logging import exception
import pyautogui
from time import sleep
from base_handlers import data_sanatizer as data_san
from base_handlers import terminal_logger as term_log


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

    def receive_a_kid(self) -> Kid:
        kid = Kid(
            input('<<< Insira o nome: '),
            input('<<< Insira a idade: '),
            date(date.year, int(input('mês: ')), int(input('dia: '))
            ),
            date(date.year, int(input('mês: ')), int(input('dia: '))
            ),
            int(input('Insira o apartamento: ')),
            input('Insira o responsável: '))
        return kid

    def add_kid_to_sector(self, kid: Kid):
        try:
            if kid.years_old <= 5 and kid.years_old > 2:
                self.kids_sector_list['clubinho'].append(kid)
                return
            if kid.years_old <= 8 and kid.years_old > 6:
                self.kids_sector_list['kids club'].append(kid)
                return
            if kid.years_old <= 13 and kid.years_old > 9:
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

    def make_kid_description(self, kid: Kid):
        sleep(5)
        kid_msg = (str(kid.name), str(kid.apt), str(kid.parents))
        pyautogui.click()
        for item in kid_msg:
            pyautogui.typewrite(item, 0.3)
            pyautogui.typewrite(' ', 0.3)
        pyautogui.hotkey('ctrl', 'enter')

        

class Jason:
    """Classe que une input, processamento, análise e output, de tudo. Ela funciona com base em composição. As duas classes que compoem essa
    são receiver e writer"""
    def __init__(self, name: str = 'Jason Mock'):
        self.name = name 


if __name__ == '__main__':
    import unittest 

    class TestReceiver(unittest.TestCase):
        receiver = Receiver()
        # def test_receive_a_kid(self):
        #     print(self.receiver.receive_a_kid())
        
        def test_add_kid_to_sector(self):
            kid = Kid()
            self.receiver.add_kid_to_sector(kid)
            self.assertIn(kid, self.receiver.kids_sector_list['clube'])
            print(self.receiver.kids_sector_list)
        
    class TestWriter(unittest.TestCase):
        my_writer = Writer()

        def test_make_kid_description(self):
            kid = Kid()
            sleep(2)
            pyautogui.hotkey('ctrl', 'n')
            sleep(2)
            self.my_writer.make_kid_description(kid)

    class TestJason(unittest.TestCase):
        pass

    unittest.main()