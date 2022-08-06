from dataclasses import dataclass
from datetime import date
import pyautogui
import json as jsn

from logging import exception
from time import sleep
from base_handlers import data_sanatizer as ds


@dataclass
class Kid:
    name: str
    years_old: int
    check_in: date
    checkout: date
    apt: int
    parent: str
    anot: str

    def make_dict(self):
        return {
        'nome': self.name,
        'idade': self.years_old,
        'check-in':[self.check_in.day, self.check_in.month],
        'check-out':[self.checkout.day, self.checkout.month],
        'apt': self.apt,
        'responsavel': self.parent,
        'anot': self.anot}


@dataclass
class Sector:
    name: str
    kids: list[Kid]
    year_limit: list[int, int]

    def add_a_kid(self, kid: Kid) -> False:
        if kid.years_old < self.year_limit[0] or kid.years_old > self.year_limit[1]: return False
        else:
            self.kids.append(kid)
            return True

    def make_dict(self):
        return {self.name: self.kids}


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

    def define_data(self, title) -> list:
        print(f'\n            {title}              \n')
        return [ds.DataInputSanatizer.filter_num('mês: '), ds.DataInputSanatizer.filter_num('dia: ')]

    def receive_a_kid(self) -> dict:
        kid = {
            'nome': input('<<< Insira o nome: '),
            'idade': ds.DataInputSanatizer.filter_num('<<< Insira a idade: '),
            'check-in':[self.define_data()],
            'check-out':[self.define_data()],
            'apt': ds.DataInputSanatizer.filter_num('Insira o apartamento: '),
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

    def store_in_data(self, open_form: str = '+w'):
        jason_objt = jsn.dumps(self.my_receiver.kids_sector_list, indent=3)
        with open('data/kids_data.json', open_form) as kids_db:
            kids_db.write((f'{jason_objt}'))

    def get_from_data(self):
        with open('data/kids_data.json') as archive:
            archive = jsn.load(archive)
        return archive


if __name__ == '__main__':
    from unittest import TestCase, main
    from writers import test_tools
    from base_handlers import terminal_logger as t_l


    kid = Kid('Alexandre', 10, date(2022, 2, 12), date(2022, 2, 18), 100, 'Rodrigo', 'Nenhuma')
    kid_mock = kid.make_dict()


    class TestSector(TestCase):
        sector = Sector('mock sector', [kid_mock], [9, 13])
        def test_make_dict(self):
            t_l.TerminalLogger.write('testando make_dict in test sector')
            print(self.sector.make_dict())

        def test_add_a_kid(self):
            t_l.TerminalLogger.write('testando receive_a_kid')
            self.assertEqual(self.sector.add_a_kid(kid), True)

    class TestKid(TestCase):
        def test_make_dict(self):
            t_l.TerminalLogger.write('testando make dict in test kid')
            print(kid.make_dict())

    class TestReceiver(TestCase):
        receiver = Receiver()
        def test_define_data(self):
            t_l.TerminalLogger.write('teste_define_data pulado: teste escrito nos testes de usabilidade')

        def test_receive_a_kid(self):
            t_l.TerminalLogger.write('teste receive_a_kid pulado: teste escrito nos testes de usabilidade')

        def test_add_kid_to_sector(self):
            t_l.TerminalLogger.write(f'verificando se {kid_mock["nome"]} será adicionado ao clube...')
            t_l.TerminalLogger.write(f'Dados: {self.receiver.kids_sector_list}')
            self.receiver.add_kid_to_sector(kid_mock)
            self.assertIn(kid_mock, self.receiver.kids_sector_list['clube'])
            t_l.TerminalLogger.write(f'Dados: {self.receiver.kids_sector_list}')


    class TestWriter(TestCase):
        writer = Writer()
        def test_make_kid_descriptions(self):
            t_l.TerminalLogger.write('Escrevendo a descrição das crianças: ')
            test_tools.prepare_archive()
            self.writer.make_kid_description(kid_mock)
            test_tools.close_arquive()
    

    class TestJason(TestCase):
        jason = Jason()

        def test_get_from_data(self):
            t_l.TerminalLogger.write('Testando get_from_data')
            self.jason.my_receiver.add_kid_to_sector(kid_mock)
            self.jason.store_in_data()
            print(self.jason.get_from_data())

        def test_store_in_data(self):
            t_l.TerminalLogger.write('testando store_in_data')
            self.jason.my_receiver.add_kid_to_sector(kid_mock)
            self.jason.my_receiver.add_kid_to_sector(kid_mock)
            self.jason.store_in_data()
            kid_mock['nome'] ='Diego'
            self.jason.store_in_data()

    main()