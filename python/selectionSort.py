# Selection Sort
import unittest
# runtime: O(n^2)

# find smallest, sawp with first element
# find second smallest, swap with second element
# find nth smallest, swap w/ n

# find smallest element of sequence and exchange it with


def selectionSort(sequence):
    """
    Input: unsorted sequence {a1, a2, a3, ... an}
    Output: permutation of the input sequence such that {a1 <= a2 <= a3 ... an}
    """

    for i in range(0, len(sequence)):
        # Set the min to initial item
        smallest = i

        # Check the rest to see if anything is smaller
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[smallest]:
                smallest = j
        if i != smallest:
            sequence[i], sequence[smallest] = sequence[smallest], sequence[i]
    return sequence

class TestSelectionSort(unittest.TestCase):
    """test selectionSort"""
    def test_sorting(self):
        example_input = [2, 1, 3, 4]
        selectionSort(example_input)
        self.assertEqual(example_input, [1,2,3,4])
    def test_return(self):
        example_input = [2, 1, 3, 4]
        sorted_array = selectionSort(example_input)
        self.assertEqual(sorted_array, [1,2,3,4])

if __name__ == '__main__':
    unittest.main()