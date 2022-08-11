from base_handlers import terminal_logger as t_l
import unittest


class TestTermminalLogger(unittest.TestCase):
    def test_something(self):
        t_l.TerminalLogger.write('Isso aqui é um teste')

if __name__ == '__main__':
    unittest.main()