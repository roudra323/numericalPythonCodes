from math import pi
import math


def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    y = [0 for i in range(n+1)]
    y[0] = f(a)
    y[n] = f(b)
    result = h*(y[0]+y[n])/2
    for i in range(1, n):
        xi = a + i*h
        y[i] = f(xi)
        result += h*y[i]
    return result


def f(x): return math.exp(x)


n = 4  # number of subintervals

# ---------------range of integration 0 to pi/2
numerical = trapezoidal(f, 0, pi/2, n)
print(numerical)
