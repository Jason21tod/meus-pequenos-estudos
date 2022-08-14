import pyautogui
import json as jsn
import logging
import os

from dataclasses import dataclass
from datetime import date
from time import sleep
from base_handlers import data_sanatizer as ds
import writers.text_cumpriments as txt_cump
from writers.text_warnings import make_generic_warning


jason_logger = logging.getLogger('Jason Pastoleiro Log')
jason_logger.setLevel(logging.INFO)

logging.basicConfig(filename='.logs.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
if __name__ == '__main__':
    jason_logger.setLevel(logging.DEBUG)
    jason_logger.debug('Iniciando testes no Jason Pastoleiro')
else:
    jason_logger.info(f'importando {__name__}...')

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


def turn_in_dataclass(kid_dict: dict):
     return Kid(
        name= kid_dict['nome'],
        years_old= kid_dict['idade'],
        check_in= date(2022, kid_dict['check-in'][1], kid_dict['check-in'][0]),
        checkout=  date(2022, kid_dict['check-out'][1], kid_dict['check-out'][0]),
        apt = kid_dict['apt'],
        parent= kid_dict['responsavel'],
        anot = kid_dict['anot'])


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
        month = ds.DataInputSanatizer.filter_month()
        day = ds.DataInputSanatizer.filter_num('dia: ')
        return [day, month]

    def receive_a_kid(self) -> dict:
        kid = {
            'nome': input('<<< Insira o nome: '),
            'idade': ds.DataInputSanatizer.filter_num('<<< Insira a idade: '),
            'check-in':[],
            'check-out':[],
            'apt': ds.DataInputSanatizer.filter_num('Insira o apartamento: '),
            'responsavel': input('Insira o responsável: ')}
        kid['check-in'] = self.make_checkin_data()
        kid['check-out'] = self.make_checkout_data(kid['check-in'])
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
            Exception(ValueError('Erro, a criança não foi adicionada em nenhum setor, verifique a idade.'))

    def make_checkin_data(self):
        while True:
            check_in = self.define_data('Check in') 
            verify_check_in_coerence = ds.CheckInOutVerifier.verify_checkin_data(check_in[1], check_in[0])
            verify_month_coerence = ds.CheckInOutVerifier.verify_month_coerence(check_in)
            if verify_check_in_coerence == False and verify_month_coerence == False:
                break
        return check_in

    def make_checkout_data(self, checkin: list = [ds.CURRENT_DAY, ds.CheckInOutVerifier.month_to_number_dict[ds.CURRENT_MONTH]]):
        while True:
            checkout = self.define_data('checkout')
            verify_month_coerence = ds.CheckInOutVerifier.verify_month_coerence(checkout)
            verify_checkout_coerence = ds.CheckInOutVerifier.verify_checkout(checkin, checkout)
            if verify_checkout_coerence == False and verify_month_coerence == False:
                break
        return checkout


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
            pyautogui.write(item, 0.03)
            pyautogui.write(' ', 0.03)
        pyautogui.hotkey('ctrl', 'enter')
        

class Jason:
    """Classe que une input, processamento, análise e output, de tudo. Ela funciona com base em composição. As duas classes que compoem essa
    são receiver e writer"""
    def __init__(self, name: str = 'Jason Mock'):
        self.name = name
        self.my_receiver: Receiver = Receiver()
        self.my_writer: Writer = Writer()

    def _store_in_data(self, open_form: str = '+w'):
        jason_objt = jsn.dumps(self.my_receiver.kids_sector_list, indent=3)
        with open('data/kids_data.json', open_form) as kids_db:
            kids_db.write((f'{jason_objt}'))

    def _get_from_data(self):
        with open('data/kids_data.json') as archive:
            archive = jsn.load(archive)
            self.my_receiver.kids_sector_list = archive
        return archive

    def receive_and_add_to_database(self):
        print('Recebendo crianças')
        print(self._get_from_data())
        self.my_receiver.add_kid_to_sector(self.my_receiver.receive_a_kid())
        jason_logger.log(logging.INFO, 'Adicionando crianca...')
        self._store_in_data()

    def delete_last_addicted(self, sector: str, ):
        print('Deletando ...')
        self._get_from_data()
        print(self.my_receiver.kids_sector_list[sector][-1])

    def make_list_kids(self, sector_string):
        self._get_from_data()
        kids = self.my_receiver.kids_sector_list
        sleep(5)
        if len(self.my_receiver.kids_sector_list[sector_string]) == 0:
            make_generic_warning(f' N tem amiguinhos no {sector_string} ! :O')
        for kid in kids[sector_string]:
            print(kid)
            sleep(2)
            self.my_writer.make_kid_description(kid)