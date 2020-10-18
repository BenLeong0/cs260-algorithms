def stablesort(a,k,n):
    queues = [[] for i in range(k)]
    for element in a:
        queues[int(element[-1-n])].append(element)
    sorted = []
    for queue in queues:
        sorted += queue
    return sorted


def radixsort(a,k=10,d=3):
    a = ['0'*(d-len(str(i))) + str(i) for i in a]
    for n in range(d):
        a = stablesort(a,k,n)
        print(a)
    sorted = []
    for x in a:
        sorted.append(int(x))
    return sorted

a = [329,457,657,839,436,720,355,100]
print(radixsort(a))
