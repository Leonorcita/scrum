import unittest
from operaciones import sumar

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
