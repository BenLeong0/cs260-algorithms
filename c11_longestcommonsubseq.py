A = 'XMJYAUZ'
B = 'MZJAWXU'
# C = 'MJAU'


def LCS(A, B):
    M = [[0 for b in B] for a in A]
    for i in range(len(A)):
        for j in range(len(B)):
            M[i][j] = max(M[max(0, i-1)][j], M[i][max(0, j-1)])
            if A[i] == B[j]:
                print(A[i], i, j)
                M[i][j] = max(M[i][j], M[max(0, i-1)][max(0, j-1)]+1)
    for row in M:
        print(row)
    return M[-1][-1]


print(LCS(A,B))
