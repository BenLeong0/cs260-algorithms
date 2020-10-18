def countingsort(a, k):
    queues = [[] for i in range(k)]
    for x in a:
        queues[x].append(x)
    sorted = []
    for queue in queues:
        sorted += queue
    return sorted


a = [1,6,7,1,3,4,9,7,8,5,12,12,16,18,6,7,19,1]
k = max(a) + 1

print(countingsort(a, k))
