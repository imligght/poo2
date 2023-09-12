def ordinate(array):
    if len(array) <= 1:
        return array

    pivot = len(array) // 2
    left = [x for x in array if x < array[pivot]]
    middle = [x for x in array if x == array[pivot]]
    right = [x for x in array if x > array[pivot]]

    return ordinate(left) + middle + ordinate(right)

arr = [4, 32, 42, 19, 16, 90, 74, 44, 6, 99, 89, 26, 23, 45, 94, 61, 98, 97, 69, 55, 86, 58, 90, 20, 55, 6, 62, 28, 32, 28, 34, 57, 92, 22, 80, 63, 96, 82, 61, 67, 34, 88, 60, 45, 24, 45, 94, 84, 17, 1]

array_ordenado = ordinate(arr)
print(array_ordenado)