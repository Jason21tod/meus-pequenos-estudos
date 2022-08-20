import os

from datetime import date
from unittest import TestCase, main
from jason_pastoleiro import Jason, Kid, Receiver, Sector, turn_in_dataclass

def clear_db(db: Jason, sector: str):
    for qunt in range(len(db.my_receiver.kids_sector_list[sector])):
        db.delete_last_addicted(sector)


kid = Kid('Alexandre', 10, date(2022, 2, 12), date(2022, 2, 18), 100, 'Rodrigo', 'Nenhuma')
kid_2 = Kid('Fernando', 12, date(2022, 2, 10), date(2022, 3, 1), 134, 'Claudia', 'Alergico a banana')
kid_mock = kid.make_dict()
kid_mock_2 = kid_2.make_dict()
for var in os.environ:
    print(var)

class test_Sector(TestCase):
    sector = Sector('mock sector', [kid_mock], [9, 13])
    def test_make_dict(self):
        print(self.sector.make_dict())

    def test_add_a_kid(self):
        self.assertEqual(self.sector.add_a_kid(kid), True)


class TestKid(TestCase):
    def test_make_dict(self):
        print(kid.make_dict())

    def test_turn_in_dataclass(self):
        turn_in_dataclass(kid_mock)


class TestReceiver(TestCase):
    receiver = Receiver()
    def test_add_kid_to_sector(self):
        print(f'verificando se {kid_mock["nome"]} será adicionado ao clube...')
        print(f'Dados: {self.receiver.kids_sector_list}')
        self.receiver.add_kid_to_sector(kid_mock)
        self.assertIn(kid_mock, self.receiver.kids_sector_list['clube'])
        print(f'Dados: {self.receiver.kids_sector_list}')


class TestJason(TestCase):
    jason = Jason()

    def test_get_from_data(self):
        print('Testando get_from_data')
        print(self.jason.my_receiver.kids_sector_list)
        self.jason.my_receiver.add_kid_to_sector(kid_mock)
        self.jason._store_in_data()
        print(self.jason.my_receiver.kids_sector_list)
        self.jason._get_from_data()

    def test_store_in_data(self):
        print('testando store_in_data')
        self.jason.my_receiver.add_kid_to_sector(kid_mock)
        self.jason.my_receiver.add_kid_to_sector(kid_mock_2)
        self.jason._store_in_data()
        clear_db(self.jason, 'clube')
        print(self.jason.my_receiver.kids_sector_list)
    
    def test_delete_the_last(self):
        print('testando delete_the_last')
        self.jason.my_receiver.add_kid_to_sector(kid_mock)
        self.jason.my_receiver.add_kid_to_sector(kid_mock_2)
        self.jason._store_in_data()
        print(self.jason.my_receiver.kids_sector_list)
        self.jason.delete_last_addicted('clube')
        print(self.jason.my_receiver.kids_sector_list)
        clear_db(self.jason, 'clube')



if __name__ == '__main__':
    main()