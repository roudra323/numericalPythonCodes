# newtons backward interpolation

def backwordInterpolation(n, x, y, value):

    def prod_cal(p, n):
        product = p
        for i in range(1, n):
            product = product*(p+i)
        return product

    def fact(n):
        f = 1
        for i in range(2, n + 1):
            f *= i
        return f

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    for i in range(n):
        print(x[i], end="\t")
        for j in range(n - i):
            print(y[i][j], end="\t")
        print(" ")

    sum = y[n-1][0]
    p = (value - x[n-1]) / (x[1] - x[0])
    for i in range(1, n):
        sum = sum + (prod_cal(p, i) * y[n-i-1][i]) / fact(i)

    return value, sum


x = [15, 20, 25, 30, 35, 40]  # x values
n = len(x)  # Number of values

y = [[0.0 for i in range(n)] for j in range(n)]  # y values
y[0][0] = 0.2588190
y[1][0] = 0.3420201
y[2][0] = 0.4226183
y[3][0] = 0.5000000
y[4][0] = 0.5735764
y[5][0] = 0.6427876


value = 38  # find the value of y(8)


value, sum = backwordInterpolation(n, x, y, value)
print("\nValue at", value,
      "is", round(sum, 6))
