import random


def pick_pivot(n):
    # return 0
    return n-1
    return random.randrange(0, n)
    return int(n/2)


def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = pick_pivot(len(list))
    pivot_value = list[pivot]
    left, right = [], []
    for val in list[:pivot] + list[pivot+1:]:
        if val < pivot_value:
            left.append(val)
        else:
            right.append(val)
    return quicksort(left) + [pivot_value] + quicksort(right)


a = [3,8,3,8,9,-3,2,8,7,4]

print(quicksort(a))
