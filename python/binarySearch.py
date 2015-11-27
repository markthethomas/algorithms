# Recursive Binary Search

def binarySearch(target, arr, minimum=0, maximum=None):
    """
    Accepts: a target element and a sorted array to search
    Returns: True if element is present, False if not
    """

    # Because we use the maximum later but don't require it as a formal parameter,
    # conditionally set it
    if maximum == None:
        maximum = len(arr)

    # Guess should be the floored average of the min and max
    guess = (minimum + maximum) // 2

    # If the initial guess is correct, return True
    if arr[guess] == target:
        return True

    # If the maxium is the same as the minimum OR greater than, the element
    # isn't present
    if maximum <= minimum:
        return False

    # If the guess is too low, set minimum to be just above the guess index
    # and guess from there
    if arr[guess] < target:
        minimum = guess + 1
        return binarySearch(target, arr, minimum, maximum)

    # If the guess is above the target, set minimum to be just below the guess
    # index and guess from there
    if arr[guess] > target:
        maximum = guess - 1
        return binarySearch(target, arr, minimum, maximum)


def test():
    rangeList = list(range(1, 99999))
    for value in rangeList:
        if binarySearch(value, rangeList) == False:
            print('Failure!')

# Downside: stack size limitations