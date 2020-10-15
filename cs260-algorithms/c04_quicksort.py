import random

def pick_pivot(l,r):
    # return 0
    # return r
    # return int((l+r)/2)
    return random.randrange(l, r+1)


def partition(a,l,r):
    b = a[:]
    pos = pick_pivot(l,r)
    pivot = b.pop(pos)
    left, right = [], []
    for x in b[l:r]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    p = len(left) + l
    return a[:l] + left + [pivot] + right + a[r+1:], p

def quicksort(a,l,r):
    if r <= l:
        return a
    a, p = partition(a,l,r)
    a = quicksort(a,l,p-1)
    a = quicksort(a,p+1,r)
    return a


a = [7,6,11,9,4,86,3,4,1,24]
# a = [0,1,2,4]
l = 0
r = len(a) - 1

print(a, '==>', quicksort(a,l,r))
