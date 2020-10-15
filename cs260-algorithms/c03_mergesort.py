def merge(b,c):
    if len(b) == 0:
        return c
    if len(c) == 0:
        return b
    if b[0] < c[0]:
        return [b[0]] + merge(b[1:], c)
    else:
        return [c[0]] + merge(b, c[1:])


def mergesort(a):
    length = len(a)
    if length <= 1:
        return a
    else:
        return merge(mergesort(a[:int(length/2)]), mergesort(a[int(length/2):]))

a = [7,6,1,9,4,86,3,4,1,24]
print(mergesort(a))
