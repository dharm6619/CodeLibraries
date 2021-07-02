def count(X, Y, m, n):
    if m == 1 and n == 1:
        return 1 if (X[0] == Y[0]) else 0
    if m == 0:
        return 0
    if n == 0:
        return 1
    if n > m:
        return 0
    return (count(X, Y, m - 1, n - 1) if X[m - 1] == Y[n - 1] else 0)\
        + count(X, Y, m - 1, n)


X = input()
Y = "HSL"
print(count(X, Y, len(X), len(Y)))