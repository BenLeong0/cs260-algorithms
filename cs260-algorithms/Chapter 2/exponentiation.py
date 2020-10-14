def power(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a
    t = power(a, int(n/2))
    if n % 2 == 0:
        return t ** 2
    else:
        return a * t ** 2


print(power(4,19))
