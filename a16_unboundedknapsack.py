items = [(1,1), (4,2), (7,3), (10,5)]
max_weight = 8


def knapsack(items, max_weight):
    K = []
    for w in range(max_weight+1):
        weight = 0
        for item in items:
            if w - item[1] >= 0:
                weight = max(K[w - item[1]] + item[0], weight)
        K.append(weight)
    return K[max_weight]


print(knapsack(items, max_weight))
