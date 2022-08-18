from typing import Any
from datetime import date, datetime


CURRENT_MONTH = datetime.now().ctime().split()[1]
CURRENT_DAY =int( datetime.now().ctime().split()[2])


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

    @classmethod
    def receive_date_from_request(self, date):
        pass

class CheckInOutVerifier:
    number_to_month_dict = {
        1: 'Jan',2: 'Feb',3: 'Mar',4: 'Apr',5: 'May',6: 'Jun',
        7: 'Jul',8: 'Aug',9: 'Sep',10: 'Oct',11: 'Nov',12: 'Dec'
    }

    month_to_number_dict = {
        'Jan':1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun':6,
        'Jul': 7, 'Aug': 8, 'Sep':9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }

    month_day_thirty_one = [1, 3, 5, 7, 8, 12]
    month_day_thirty = [4, 6, 9, 10, 11]

    @classmethod
    def verify_checkin_data(cls, month: int, day:int):
        if day < 1: 
            print('O dia não pode ser menor que zero !')
            return True
        if month > cls.month_to_number_dict[CURRENT_MONTH]:
            print(f' O mes de checkin n pode ser maior q o mes atual: {cls.month_to_number_dict[CURRENT_MONTH]}')
            return True
        if month == cls.month_to_number_dict[CURRENT_MONTH]:
            if day > CURRENT_DAY:
                print('O dia não pode ser maior que o atual se o checkin é esse mes !')
                return True
        return False

    @classmethod
    def verify_month_coerence(cls, month_data: list):
        try:
            if month_data[0] < 1:
                return True
            if month_data[1] in cls.month_day_thirty_one:
                if month_data[0] > 31:
                    print('O mes n tem mais que 31 dias gente ')
                    return True
            if month_data[1] == 2:
                if month_data[0] > 29:
                    print('fevereiro n tem mais q 29 dias')
                    return True
            if month_data[1] in cls.month_day_thirty:
                if month_data[0] > 30:
                    print('Esse mes n tem mais q 30 dias')
                    return True
        except:
            raise ValueError(f'Os dados do checkout estão errados {month_data}')
        return False

    @classmethod
    def verify_checkout(cls, checkin, checkout):
        if checkin[1] > checkout[1]:
            print('O mes do checkout deve ser maior q o do checkin :o')
            return True
        if checkout[1] < cls.month_to_number_dict[CURRENT_MONTH]:
            print('Esse hospede ja foi embora ???')
            return True
        else:
            if checkin[1] == checkout[1]:
                if checkin[0] > checkout[0]: 
                    print('O dia do checkout n tem como ser menor que o dia do checkin no mesmo mes !')
                    return True

        return False
