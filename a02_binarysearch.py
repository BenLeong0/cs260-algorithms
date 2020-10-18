import random


def binary_search(array, n):
    mid = int(len(array)/2)
    if n == array[mid]:
        return mid
    elif len(array) == 1:
        return 'NOT FOUND'
    elif n > array[mid]:
        if len(array) == 2:
            return 'NOT FOUND'
        elif binary_search(array[mid+1:], n) == 'NOT FOUND':
            return binary_search(array[mid+1:], n)
        else:
            return mid + 1 + binary_search(array[mid+1:], n)
    elif n < array[mid]:
        return binary_search(array[:mid], n)

# Example array
x = [0,2,5,9,13]

print(binary_search(x, 0))
print(binary_search(x, 2))
print(binary_search(x, 4))
print(binary_search(x, 19))
print(binary_search(x, 13))
print(binary_search(x, 12))
