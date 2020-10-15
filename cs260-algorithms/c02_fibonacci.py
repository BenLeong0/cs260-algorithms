def matrix_mult(m,n):
    a,b,c,d = m[0][0], m[0][1], m[1][0], m[1][1]
    e,f,g,h = n[0][0], n[0][1], n[1][0], n[1][1]
    w = a*e + b*g
    x = a*f + b*h
    y = c*e + d*g
    z = c*f + d*h
    return [[w,x],[y,z]]


def power(a,n):
    if n == 0:
        return [[1,0],[0,1]]
    if n == 1:
        return a
    t = power(a, int(n/2))
    if n % 2 == 0:
        return matrix_mult(t, t)
    else:
        return matrix_mult(a, matrix_mult(t, t))


n = 60
M = power([[1,1],[1,0]], n-1)
print(M[0][0])
