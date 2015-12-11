import unittest
import sys

"""
Problem Statement:

Given a squared sized grid G of size N in which each cell has a lowercase letter. Denote the character in the ith row and in the jth column as G[i][j].

You can perform one operation as many times as you like: Swap two column adjacent characters in the same row G[i][j] and G[i][j+1] for all valid i,j.

Is it possible to rearrange the grid such that the following condition is true?

G[i][1]≤G[i][2]≤⋯≤G[i][N] for 1≤i≤N and
G[1][j]≤G[2][j]≤⋯≤G[N][j] for 1≤j≤N
In other words, is it possible to rearrange the grid such that every row and every column is lexicographically sorted?

Note: c1≤c2, if letter c1 is equal to c2 or is before c2 in the alphabet.

Input Format:
The first line begins with T, the number of testcases. In each testcase you will be given N. The following N lines contain N lowercase english alphabet each, describing the grid.

Output Format:
Print T lines. On the ith line print YES if it is possible to rearrange the grid in the ith testcase or NO otherwise.
"""


def lexSortableGrid(grid):
    for i in range(len(grid)):
        currentRow = list(grid[i][0])
        grid[i] = sorted(currentRow)
    for row in range(len(grid) - 1):
        for col in range(len(grid[row]) - 1):
            if grid[row][col] < grid[row + 1][col] and grid[row][col] < grid[row][col + 1]:
                pass
            else:
                print('NO')
                return False
    print('YES')
    return True

testGrid = [['ebacd'],
            ['fghij'],
            ['olmkn'],
            ['trpqs'],
            ['xywuv']]

lexSortableGrid(testGrid)

class TestLexSortableGrid(unittest.TestCase):
    """test LexSortableGrid"""

    def TestSort1(self):
        testGrid2 = [['ppp'], ['ypp'], ['wyw']]
        self.assertEqual(lexSortableGrid((testGrid2)), True)

    def TestSort1(self):
        testGrid2 = [['ppp'], ['ypp'], ['wyw']]

    def testSort2(self):
        testGrid = [['ebacd'],
                    ['fghij'],
                    ['olmkn'],
                    ['trpqs'],
                    ['xywuv']]
        self.assertEqual(lexSortableGrid((testGrid)), True)

if __name__ == '__main__':
    unittest.main()
