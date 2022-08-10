import jason_pastoleiro
import unittest


class JasonUseCases(unittest.TestCase):
    jason_fake = jason_pastoleiro.Jason()

    def test_define_data(self):
        self.jason_fake.my_receiver.define_data('definindo os dados de check-in')
    
    def test_receive_a_kid(self):
        self.jason_fake.my_receiver.receive_a_kid()
    
    def test_receive_and_add(self):
        self.jason_fake.receive_and_add_to_database()
        print(self.jason_fake.my_receiver.kids_sector_list)

unittest.main()
