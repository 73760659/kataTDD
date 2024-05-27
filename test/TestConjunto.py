import unittest
from SRC.logica.conjunto import Conjunto

class MyTestCase(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])

        self.assertIsNone(conjunto.promedio())


if __name__ == '__main__':
    unittest.main()
