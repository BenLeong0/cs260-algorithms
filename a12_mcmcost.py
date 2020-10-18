from math import inf

M = [40,20,30,10,30]
M = [10,20,30,40,30]
M = [10,20,30]


def MCMcost(M):
    n = len(M) - 1
    C = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        C[i][i] = 0
    for l in range(n):
        for i in range(n-l):
            j = i + l
            for t in range(i, j+1):
                C[i][j] = min(C[i][j], C[i][t-1] + C[t][j] + M[i-1]*M[t-1]*M[j])
    for row in C:
        print(row)
    return C[0][-1]


print(MCMcost(M))
