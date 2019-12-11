#!/usr/bin/env python3

import unittest

from functions import fuel_calculator, fuel_calculator_part_two

class MyTest(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(fuel_calculator(10), 1)
        self.assertEqual(fuel_calculator(12), 2)
        self.assertEqual(fuel_calculator(1969), 654)
        self.assertEqual(fuel_calculator(100756), 33583)

    def test_part_two(self):
        self.assertEqual(fuel_calculator_part_two([14]), 2)
        self.assertEqual(fuel_calculator_part_two([1969]), 966)
        self.assertEqual(fuel_calculator_part_two([100756]), 50346)

if __name__ == '__main__':
    unittest.main()
