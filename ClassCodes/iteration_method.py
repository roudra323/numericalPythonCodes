def iteration(g, p0, TOL, N0):
    i = 1
    while i <= N0:
        p = g(p0)
        print(format(i, '3d'), '  ', format(p0, '10.8f'),
              '  ', format(abs(p-p0), '10.2e'))
        if abs(p-p0) < TOL:
            return print('The solution is ', p)
        i = i+1
        p0 = p
    print(f'The method fails after {N0} iterations')
    return None


#def g1(x): return x - x**3-4*x**2 + 10
def g2(x): return (10/x-4*x)**0.5
def g3(x): return 0.5*(10-x**3)**0.5
def g4(x): return (10/(4+x)**0.5)
def g5(x): return x-(x**3-4*x**2-10)/(3*x**2+8*x)


#iteration(g1, 1.5, .0001, 250)
iteration(g2, 1.5, .0001, 35)
iteration(g3, 1.5, .0001, 250)
iteration(g4, 1.5, .0001, 250)
iteration(g5, 1.5, .0001, 250)
