""" 
Objective: Writing a unit test for a this `Simple Calculator` class that supports
addition, substraction, multiplication and division operations.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

        # Set up the SimpleCalculator instance beforeeach test.
    def setUp(self):
        self.calc = SimpleCalculator()

    
        # Test the addition method.
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(0,0), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

        # Test the subtraction method 
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 1), -1)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    # Test the multiplication method 
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 1), 0)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    # Test the Division method 
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(-6, -3), 2)



if __name__ == "__main__":
    unittest.main()