from heand import hand
import math
import unittest



class Test_func(unittest.TestCase):
    def test_different_positive_integers(self):
        self.assertEqual((4, 1, 9), (math.sqrt(3) / 3) + 3)

    def test_division_by_zero(self):
        self.assertEqual((2, 2, 4), "Деление на ноль")

    def test_negative_under_sqrt(self):
        self.assertEqual((1, 3, 9), "Недопустимое значение под корнем")
        self.assertEqual((5, 3, -4), "Недопустимое значение под корнем")

    def test_floating_point(self):
        self.assertEqual((0.1, 0.2, 0.3), "Недопустимое значение под корнем")
        self.assertEqual((0.2, 0.1, 0.3), (math.sqrt(0.1) / 0.1) + math.sqrt(0.3))

if __name__ == "__main__":
    unittest.main()
