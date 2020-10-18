a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
L = [1]
S = [[a[0]]]

for i in range(1, len(a)):
    L.append(1)
    S.append(a[i])
    for j in range(i):
        if a[j] < a[i] and L[j] + 1 > L[i]:
            L[i] = L[j] + 1
            S[i] = S[j] + [a[i]]

print(S[L.index(max(L))], '- length:', max(L))
