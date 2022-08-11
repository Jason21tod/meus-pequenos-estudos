from base_handlers import data_sanatizer as d_t
from datetime import date
import unittest

class TestDataInputSanatizer(unittest.TestCase):
    def test_verify_is_number(self):
        self.assertEqual(d_t.DataInputSanatizer.verify_is_number('B'), False)
        self.assertEqual(d_t.DataInputSanatizer.verify_is_number(2), True)
    
    def test_filter_date_numbers(self):
        date_mock = date(2022, 12, 12)
        print(d_t.DataInputSanatizer.filter_date_numbers(date_mock))

    def test_verify_is_in_month_limit(self):
        self.assertEqual(d_t.DataInputSanatizer.verify_is_in_month_limit(1), True)
        self.assertEqual(d_t.DataInputSanatizer.verify_is_in_month_limit(13), False)
        self.assertEqual(d_t.DataInputSanatizer.verify_is_in_month_limit(0), False)
    
class TestCheckInOutHandler(unittest.TestCase):

    def test_verify_check_in_data(self):
        print('Data atual: ', d_t.CURRENT_MONTH, d_t.CURRENT_DAY)
        self.assertEqual(d_t.CheckInOutVerifier.verify_checkin_data(d_t.CheckInOutVerifier.month_to_number_dict[d_t.CURRENT_MONTH]-1, d_t.CURRENT_DAY-1), True)

    def test_verify_checkout_data(self):
        self.assertEqual(d_t.CheckInOutVerifier.verify_month_coerence([31, 11]), True)
        self.assertEqual(d_t.CheckInOutVerifier.verify_month_coerence([30, 2]), True)
        self.assertEqual(d_t.CheckInOutVerifier.verify_month_coerence([0, 8]), True)
        self.assertEqual(d_t.CheckInOutVerifier.verify_month_coerence([32, 8]), True)
        self.assertEqual(d_t.CheckInOutVerifier.verify_month_coerence([31, 12]), False)

    def test_verify_stay(self):
        self.assertEqual(d_t.CheckInOutVerifier.verify_checkout([10, 10], [10, 9]), True)
        self.assertEqual(d_t.CheckInOutVerifier.verify_checkout([11, 10], [10, 10]), True)
        self.assertEqual(d_t.CheckInOutVerifier.verify_checkout([10, 10], [10, 10]), False)
        self.assertEqual(d_t.CheckInOutVerifier.verify_checkout([30, 10], [10, 11]), False)


if __name__ == '__main__':
    unittest.main()

