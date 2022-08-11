from typing import Any
import unittest

_NAME = 'Jason Pastoleiro'


class TerminalLogger:
    """Um logger que escreve as ações. Usado para diferenciar as mensagens da I.A do sistema.
    é uma forma de dizer como jason está lidando com tudo."""
    @classmethod
    def write(cls, something: Any):
        print(_NAME, ' -  Avisa >>> ', something)
        print()

