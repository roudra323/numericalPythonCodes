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


#def g1(x): return x ** 3 - 1
def g2(x): return (x+1)**(1/3)


# iteration(g1,1.5,.0001,25)
#iteration(g1, 1.5, .0001, 50)
iteration(g2, 1.5, .0001, 250)
