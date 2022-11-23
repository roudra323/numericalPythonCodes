import math


def richardson(f, x, n, h):
    d = [[0 for i in range(n)] for j in range(n)]
    for i in range(n + 1):
        d[i][0] = (f(x + h) - f(x)) / h
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            d[i, j] = d[i, j-1] + (d[i, j-1] - d[i-1, j-1]) / (powerOf4 - 1)
            h = 0.5 * h
        return d


def f(a): return math.log(10, a)


x = 1.8
n = 4
h = 0.1
d = richardson(f, x, n, h)
