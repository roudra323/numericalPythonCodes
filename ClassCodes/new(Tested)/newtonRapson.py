# importing "math" for mathematical operations
import math


def NewtonRapson(f, f1, p0, TOL, N0):
    i = 0
    while i <= N0:
        p = p0-f(p0)/f1(p0)
        print(format(i, '3d'), '  ', format(p0, '10.8f'),
              '  ', format(abs(p-p0), '10.2e'))
        if abs(p-p0) < TOL:
            return print('The solution is ', p)
        i = i+1
        p0 = p
    print('The method fails after N0 iterations')
    return None


def f(x): return math.cos(x) - x  # main function


def f1(x): return - math.sin(x) - 1  # the derivative of the function


# -------^-----calculate range here from the main function
NewtonRapson(f, f1, 1, 0.0000000000000001, 20)