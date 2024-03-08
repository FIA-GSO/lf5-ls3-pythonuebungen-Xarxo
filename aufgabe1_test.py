import unittest

import main


class TestAufgabe1(unittest.TestCase):

    def test_population(self):
        result1 = (60,5,3)
        step1 = main.compute_r2d2_population(1)
        self.assertEqual(step1, result1)

        result2 = (26, 30, 1)
        step2 = main.compute_r2d2_population(2)
        self.assertEqual(step2, result2)

        result3 = (122, 13, 10)
        step3 = main.compute_r2d2_population(3)
        self.assertEqual(step3, result3)

        result4 = (72, 61, 4)
        step4 = main.compute_r2d2_population(4)
        self.assertEqual(step4, result4)

        result5 = (252, 36, 20)
        step5 = main.compute_r2d2_population(5)
        self.assertEqual(step5, result5)


if __name__ == '__main__':
    unittest.main()