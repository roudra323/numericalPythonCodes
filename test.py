# backward  interpolation formula

def prod_cal(p, n):
    temp = p
    for i in range(n):
        temp *= (p+i)
    return temp


def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans


n = 4  # Number of values
x = [1, 3, 5, 7]

y = [[0 for i in range(n)] for j in range(n)]
y[0][0] = 24
y[1][0] = 120
y[2][0] = 336
y[3][0] = 720


for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]


for i in range(n):
    print(x[i], end="\t")
    for j in range(n-i):
        print(y[i][j], end="\t")
    print(" ")


value = 8

sum = y[n-1][0]
p = (value - x[n-1])/(x[1]-x[0])

for i in range(1, n):
    sum = sum + (prod_cal(p, i) * y[n-i-1][i]) / fact(i)


print("\nValue at", value,
      "is", round(sum, 6))
