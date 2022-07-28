from dataclasses import dataclass
from datetime import date
from random import randint


@dataclass
class Kid:
    name: str ='mock kid'
    parents: str ='parents mock'
    years_old: int = 12
    apt: int = 120
    check_in: str ='12/2/22'
    check_out: str = '22/2/22'
    anot: str =''
    same_apt: str= ''


@dataclass
class Sector:
    def __init__(self, name: str ='sector mock', max_year: int= 12, min_year: int= 9) -> None:
        self.kids_list= list([Kid])
        self.name: str = name
        self.max_year: int = max_year
        self.min_year: int = min_year  
    
    def verify_a_kid(self, kid:Kid):
        if kid.years_old >= self.min_year and kid.years_old <= self.max_year:
            self.kids_list.append(kid)
            return
        else:
            return
    
    def see_every_one(self):
        print(f'\nCRIANÇAS DO {self.name}'.upper())
        for kid in self.kids_list:
            print(kid)
        print(f'Total de: {len(self.kids_list)} crianças')

    def send_msg(self, msg_title: str):
        print(msg_title.upper())
        print('Nome   apt    responsaveis    anot')
        for kid in self.kids_list:
            print(kid.name,' ', kid.apt," ", kid.parents," ",kid.anot, " ", kid.years_old)
        print(f'Total de crianças: ', len(self.kids_list))
        print('Feito pelo robozinho analista do tio mogli ^^)')
        print()

little_club = Sector('clubinho', 5, 3)
kids_club = Sector('kids club', 8, 6)
club = Sector('clube', 13, 9)


class SectorHandler:
    all_kids = [
        little_club.kids_list,
        kids_club.kids_list,
        club.kids_list
        ]

    def see_every_one(self):
        for sector in self.all_kids:
            print(sector)


if __name__ == '__main__':
    from unittest import TestCase, main

    def init_test( test_name):
        print('\ntestando: ', test_name)

    def do_a_random_kids_list(how_many: int):
        random_kids_list = []
        for kid in range(0, how_many):
            random_kids_list.append(Kid((f'criança {kid}'), (f'responsável {kid}'), randint(3, 13),randint(100, 459), randint(1,30), randint(1, 30), ''))
        return random_kids_list

    class TestKidData(TestCase):
        def test_infos(self):
            init_test(Kid())


    class TestSector(TestCase):
        def test_infos(self):
            sector_mock =Sector()
            init_test(sector_mock)

        def test_verify_a_kid(self):
            init_test('verify_a_kid')
            kid_mock = Kid()
            sector_mock = Sector()
            sector_mock.verify_a_kid(kid_mock)
            self.assertIn(kid_mock, sector_mock.kids_list)
            print(sector_mock.kids_list)

        def test_verify_in_various_sectors(self):
            init_test('verificando se a criança para em varios setores : espera-se que ela esteja em um só')
            kid_mock = Kid()
            little_club.verify_a_kid(kid_mock)
            kids_club.verify_a_kid(kid_mock)
            club.verify_a_kid(kid_mock)
            little_club.see_every_one()
            kids_club.see_every_one()
            club.see_every_one()
            little_club.kids_list.clear()
            kids_club.kids_list.clear()
            club.kids_list.clear()

        def test_multi_separation(self):
            init_test('verificando se as crianças estão em varios setores')
            kids_list = do_a_random_kids_list(100)
            for kid_mock in kids_list:
                little_club.verify_a_kid(kid_mock)
                kids_club.verify_a_kid(kid_mock)
                club.verify_a_kid(kid_mock)
            little_club.see_every_one()
            kids_club.see_every_one()
            club.see_every_one()
        
        def test_send_msg(self):
            little_club.send_msg('Clubinho na pastinha <3')
            kids_club.send_msg('Kids clube na pastinha !!!')
            club.send_msg('clubão no pastão !!!')
    
    main()

"""
    class TestSectorHandler(TestCase):
        def test_all_view(self):
            kids_list = do_a_random_kids_list(100)
            for kid_mock in kids_list:
                little_club.verify_a_kid(kid_mock)
                kids_club.verify_a_kid(kid_mock)
                club.verify_a_kid(kid_mock)
            sector_handler_mock = SectorHandler()
            sector_handler_mock.see_every_one()"""