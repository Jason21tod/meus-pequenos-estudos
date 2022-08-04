from typing import Any

_NAME = 'Jason Pastoleiro Analista'


class TerminalLogger:
    """Um logger que escreve as ações. Usado para diferenciar as mensagens da I.A do sistema.
    é uma forma de dizer como jason está lidando com tudo."""
    @classmethod
    def write(cls, something: Any):
        print(_NAME, ' -  Avisa >>> ', something)


if __name__ == '__main__':
    import unittest

    class TestTermminalLogger(unittest.TestCase):
        def test_something(self):
            TerminalLogger.write('Isso aqui é um teste')

    unittest.main()
