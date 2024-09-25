# Testa a classe Employee

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Cria um funcionário para os testes"""
    def setUp(self):
        self.first = 'silas'
        self.last = 'briarwood'
        self.salary = 65000
        self.employee = Employee(self.first, self.last, 65000)
    
    def test_give_default_raise(self):
        """Testa o aumento padrão"""
        self.assertEqual(self.employee.give_raise(), 70000)

unittest.main()