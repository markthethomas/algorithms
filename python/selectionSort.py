# Selection Sort

import unittest

# find smallest, sawp with first element
# find second smallest, swap with second element
# find nth smallest, swap w/ n

# find smallest element of sequence and exchange it with


def selectionSort(sequence):
    """
    Input: unsorted sequence {a1, a2, a3, ... an}
    Output: permutation of the input sequence such that {a1 <= a2 <= a3 ... an}
    """
    def swap(first, second, array):
        temp = first
        array[first] = array[second]
        array[second] = temp

    for i in list(range(len(sequence) - 1)):
        # Set the min to initial item
        smallest = i

        # Check the rest to see if anything is smaller
        for j in list(range(len(sequence))):
            if sequence[j] < sequence[smallest]:
                # TODO assign new min here!

    return sequence

example_input = list(range(4))

print(selectionSort(example_input))


class TestSelectionSort(unittest.TestCase):
    """ TestSelectionSort"""
    def test_sorting(self):
        unsorted_array = [2, 4, 1, 3]
        self.assertEqual(selectionSort(unsorted_array), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()