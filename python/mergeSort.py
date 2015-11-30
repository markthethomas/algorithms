"""
    Merge sort

    runtime: O(n log n)
"""

import unittest


def merge(left, right):
    # Create an empty list to put things into
    result = []

    # n is counter for left, m is counter for right (seperate indices)
    n, m = 0, 0

    # compare left and right, adding the lesser one to the result list
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1

    # Add the remaining items to the array (the end ones), if any
    result += left[n:]
    result += right[m:]
    return result


def mergeSort(sequence):

    # if the list is really short (#len() of 1), it's already sorted
    if len(sequence) <= 1:
        return sequence

    # Get a middle value
    middle = int(len(sequence) // 2)
    # recursively call merge sort on left slice of array
    left = mergeSort(sequence[:middle])
    # recursively call merge sort on right slice of array
    right = mergeSort(sequence[middle:])
    # with each passed left and right segements, call the merge function to compare each item of
    # left right and merge them together into the right order. Returns a sequence
    return merge(left, right)


class TestMergeSort(unittest.TestCase):
    """test TestMergeSort"""

    def test_sorting(self):
        example_input = [2, 1, 3, 4]
        sortedArray = mergeSort(example_input)
        self.assertEqual(sortedArray, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
