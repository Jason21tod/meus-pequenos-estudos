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
    def verify_is_in_month_limit(cls, option):
        if option >12:
            print('Este mês não existe, está mais que 12 meses >:(')
            return False
        if option <=0:
            print('Este mês não existe >:(, não existe menor que zero')
            return False
        else: return True

    @classmethod
    def filter_month(cls):
        while True:
            option = cls.filter_num('Insira o mês: ')
            if cls.verify_is_in_month_limit(int(option)): break
        return int(option)


    @classmethod
    def filter_date_numbers(self, date: date):
        return [date.year,date.month,date.day]
