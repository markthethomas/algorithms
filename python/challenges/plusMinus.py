import unittest

"""
Problem Statement:
Given an array of integers, calculate which fraction of the elements are positive, negative, and zeroes, respectively. Print the decimal value of each fraction.

Input Format:
The first line, N, is the size of the array.
The second line contains N space-separated integers describing the array of numbers (A1,A2,A3,⋯,AN).

Output Format:
Print each value on its own line with the fraction of positive numbers first, negative numbers second, and zeroes third.

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The fraction of the positive numbers, negative numbers and zeroes are 36=0.500000, 26=0.333333 and 16=0.166667, respectively.
"""


def plusMinus(arr):

    def roundToPrecision(num):
        return round(num / n, 6)

    n = len(arr)
    pos, neg, zer = 0, 0, 0
    for item in arr:
        if item == 0:
            zer += 1
        elif item > 0:
            pos += 1
        elif item < 0:
            neg += 1

    results = []

    for result in [pos, neg, zer]:
        results.append(roundToPrecision(result))

    return results


class TestPlusMinus(unittest.TestCase):

    def test_plus_minus(self):
        arr = [-4, 3, -9, 0, 4, 1]
        self.assertEqual(plusMinus(arr), [0.500000, 0.333333, 0.166667])

if __name__ == '__main__':
    unittest.main()
