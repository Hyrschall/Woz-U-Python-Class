# Lesson 9 Debugging and Unit Testing in Python
import unittest


def multiply_numbers(a, b):
    """This Function Multiplies Two Numbers Together And Stores The Result."""
    result = a * b
    return result


class TestMultiplyingNumbers(unittest.TestCase):
    """ Testing multiplyed numbers function"""

    def test_numbers(self):
        """Do you have enough numbers?"""
        numbers_multiplied = multiply_numbers(3, 4)
        self.assertEqual(numbers_multiplied, 12)

