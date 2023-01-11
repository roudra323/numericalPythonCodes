def bisection(f, a, b, TOL, N0):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    i = 1
    FA = f(a)
    print('   n', '         a', '             b',
          '             p', '            f(p)')
    while i <= N0:
        p = (a+b)/2
        FP = f(p)
        print(format(i, '>4d'), ' ', format(a, '>12.8f'), ' ', format(
            b, '>12.8f'), ' ', format(p, '>12.8f'), ' ', format(f(p), '>12.2e'))
        if FP == 0 or abs(f(p)) < TOL:
            FP = f(p)
            return print('The solution is ', p)
        i = i+1
        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print('The method fails after N0 iterations')
    return None


def f(x): return x**3-x - 1


bisection(f, 1, 2, .00001, 50)
