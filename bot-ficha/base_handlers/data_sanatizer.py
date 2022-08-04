from typing import Any
from datetime import date

class DataInputSanatizer:
    """Classe responsável por polir os dados inputados pelos usuários. Ela deve conter somente métodos 
    que visem limpar uma estrutura de dados."""
    @classmethod
    def verify_is_number(cls, option: Any) -> bool:
        try:
            float(option)
            return True
        except:
            pass
        print('Somente números são permitidos')
        return False

    @classmethod
    def filter_num(cls,msg) -> int:
        while True:
            option = input(msg)
            if cls.verify_is_number(option): break
        return int(option)

    @classmethod
    def filter_date_numbers(self, date: date):
        return [date.year,date.month,date.day]


if __name__ == '__main__':
    import unittest

    class TestDataInputSanatizer(unittest.TestCase):
        def test_verify_is_number(self):
            self.assertEqual(DataInputSanatizer.verify_is_number('B'), False)
            self.assertEqual(DataInputSanatizer.verify_is_number(2), True)
        
        def test_filter_date_numbers(self):
            date_mock = date(2022, 12, 12)
            print(DataInputSanatizer.filter_date_numbers(date_mock))

    unittest.main()