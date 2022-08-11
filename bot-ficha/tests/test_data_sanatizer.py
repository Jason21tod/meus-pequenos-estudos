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

if __name__ == '__main__':
    unittest.main()

