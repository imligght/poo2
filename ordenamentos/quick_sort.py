def ordinate(array):
    if len(array) <= 1:
        return array

    pivot = len(array) // 2
    left = [x for x in array if x < array[pivot]]
    middle = [x for x in array if x == array[pivot]]
    right = [x for x in array if x > array[pivot]]

    return ordinate(left) + ordinate(middle) + ordinate(right)

