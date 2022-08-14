import jason_pastoleiro
import unittest

class TestJasonUseCases(unittest.TestCase):
    jason_fake = jason_pastoleiro.Jason()

    def test_make_check_in_data(self):
        print(self.jason_fake.my_receiver.make_checkin_data())

    def test_make_checkout_data(self):
        print(self.jason_fake.my_receiver.make_checkout_data())

    def test_define_data(self):
        self.jason_fake.my_receiver.define_data('definindo os dados de check-in')
    
    def test_receive_a_kid(self):
        print(self.jason_fake.my_receiver.receive_a_kid())
    
    def test_receive_and_add(self):
        self.jason_fake.receive_and_add_to_database()
        print(self.jason_fake.my_receiver.kids_sector_list)


if __name__ == '__main__':
    unittest.main()
