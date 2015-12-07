import unittest

"""
Simple implementation of factorial function

time complexity: O(n)

"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):
    """docstring for TestFactorial"""

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
    unittest.main()
