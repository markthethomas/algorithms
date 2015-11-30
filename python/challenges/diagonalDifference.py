import unittest
# Given a square matrix of size N×N, calculate the absolute difference
# between the sums of its diagonals.
# 3 rows
# sample = [ [11  2  4],
#            [4   5   6],
#            [10  8 -12] ]


def diagnonalDifference(matrix):
    primaryDiagonal, secondaryDiagonal = 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                primaryDiagonal += matrix[i][j]
    for k in range(len(matrix)):
        length = len(matrix[k])
        secondaryDiagonal += matrix[k][length - k - 1]

    return abs(primaryDiagonal - secondaryDiagonal)


class TestTimeConversion(unittest.TestCase):
    """TestTimeConversion"""

    def test_conversion(self):
        sample_matrix = [[11,  2,  4],
                         [4, 5,  6],
                         [10, 8, -12]]
        self.assertEqual(diagnonalDifference(sample_matrix), 15)

if __name__ == '__main__':
    unittest.main()
