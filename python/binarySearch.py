def binarySearch(target, array):
    """
    Accepts: a target element and a *sorted* array to search
    Returns: the position of the element
    """
    if len(array) = 1:
        return array[0]
    min = 0
    middle = len(array) // 2
    max = array[-1]

    if target = array[middle]
        return middle
    if target > middle:
        min = array[middle]
        array = array[middle:]
        return binarySearch(target, array)
    if target < middle:
        min = array[0]
        array = array[:middle]
        return binarySearch(target, array)
