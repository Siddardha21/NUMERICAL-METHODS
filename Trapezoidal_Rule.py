# Trapezoidal rule
import math
import sympy as sym

def y(x):
    # Declaring the function
    fx = x/(1 + x)         # --------
    return fx


# Range of definite integral
x0 = 0
xn = 1
n = 6
# h =
# n = (xn - x0)/h

# Function to evalute the value of integral
def trapezoidal(a, b, n):
    # Grid spacing
    h = (b - a) / n

    # Computing sum of first and last terms
    # in above formula
    s = (y(a) + y(b))

    # Adding middle terms in above formula
    i = 1
    while i < n:
        s += 2 * y(a + i * h)
        i += 1

    # h/2 indicates (b-a)/2n.
    # Multiplying h/2 with s.
    return ((h / 2) * s)
print()
print("Value of integral is ",
      "%.4f" % trapezoidal(x0, xn, n))