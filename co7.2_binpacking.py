I = [0.3, 0.9, 0.5, 0.7, 0.1, 0.6, 0.2, 0.5]

def next_fit(I):
    k = 1
    s = 0
    bins = [[]]
    for i in range(len(I)):
        if s + I[i] > 1:
            k += 1
            s = 0
            bins.append([])
        bins[-1].append(I[i])
        s += I[i]
    return bins


def first_fit(I):
    bins = [[]]
    for i in range(len(I)):
        need_new = True
        for bin in bins:
            if sum(bin) + I[i] <= 1:
                bin.append(I[i])
                need_new = False
                break
        if need_new:
            bins.append([I[i]])
    return bins


def first_fit_decreasing(I):
    J = I[:]
    J.sort(reverse=True)
    return first_fit(J)




print(first_fit_decreasing(I))
