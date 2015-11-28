# Insertion sort


def insertionSort(sequence):
    """
    Input: unsorted sequence {a1, a2, a3, ... an}
    Output: permutation of the input sequence such that {a1 <= a2 <= a3 ... an}
    """
    # skip the first element
    for index in list(range(1, len(sequence))):
        # determine which item is currently being evaluated
        current = sequence[index]

        # insert into sorted sequence
        i = index - 1

        # sort subarray
        while i >= 0 and sequence[i] > current:
            # while i isn't 0 and prev item is greater than the current
            sequence[i + 1] = sequence[i]

            # decrement i
            i = i - 1

        # assign the current value i (because i is now 0)
        sequence[i + 1] = current

    return sequence


a = [3, 4, 2, 1]
sortedA = [1, 2, 3, 4]
insertionSort(a)
print('sorted √' if a == sortedA else 'not sorted :(')
