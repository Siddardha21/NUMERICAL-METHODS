# Python code for simpson's 1 / 3 rule
import math
import sympy

# Function to calculate f(x)
def func(x):

    fx = 1 / (1 + x * x)   # 1/(1+ math.log(x))
    return fx


# Driver code
a = 0  # Lower limit
b = 1  # Upper limit

# h_value = 1/4
# n = (b - a)/h_value

# Number of interval
n = 6


# Function for approximate integral
def simpsons_(ll, ul, n):
    # Calculating the value of h
    h = (ul - ll) / n

    # List for storing value of x and f(x)
    x = list()
    fx = list()

    # Calcuting values of x and f(x)
    i = 0
    while i <= n:
        x.append(ll + i * h)
        fx.append(func(x[i]))
        i += 1

    # Calculating result
    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
        i += 1
    res = res * (h / 3)
    return res



print("%.4f" % simpsons_(a, b, n))