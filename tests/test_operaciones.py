import unittest
from source.operaciones.operaciones import Operaciones


class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        operaciones = Operaciones(3, 2)
        self.assertEqual(operaciones.sumar(), 5)

    def test_restar(self):
        operaciones = Operaciones(5, 2)
        self.assertEqual(operaciones.restar(), 3)

if __name__ == '__main__':
    unittest.main()
