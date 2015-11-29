# Selection Sort

# find smallest, sawp with first element
# find second smallest, swap with second element
# find nth smallest, swap w/ n

# find smallest element of sequence and exchange it with


def selectionSort(sequence):
    """
    Input: unsorted sequence {a1, a2, a3, ... an}
    Output: permutation of the input sequence such that {a1 <= a2 <= a3 ... an}
    """

    for i in list(range(len(sequence) - 1)):
        # Set the min to initial item
        smallest = i

        # Check the rest to see if anything is smaller
        for j in list(range(len(sequence))):
            if sequence[j] <= sequence[smallest]:
                smallest = j
        print(sequence)
        temp = sequence[smallest]
        sequence[smallest] = sequence[i]
        sequence[i] = temp

example_input = [2, 1, 3, 4]
selectionSort(example_input)
print(example_input)
