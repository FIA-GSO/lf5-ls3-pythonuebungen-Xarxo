import unittest

import main


class TestAufgabe3(unittest.TestCase):

    def test_heron(self):
        result1 = 5.000023178253949
        step1 = main.heron_verfahren(25,0.01)
        self.assertEqual(step1, result1)


if __name__ == '__main__':
    unittest.main()