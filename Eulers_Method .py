import math
import sympy as sym

def f(x, y):
    fx= x**3 - 6*x**2 + 11*x - 6  # Function Input---------
    return fx
    # or fx = lambda x: x+y


# Enter initial conditions
x0 = 0.5
y0 = 0.5

xn = 1
h = 0.2
# h = (xn - x0) / n
# n =
step = ((xn - x0) / h)

# Euler method
def euler(x0, y0, xn, n):
    # Calculating step size
    h = (xn - x0) / n

    print('\n-----------SOLUTION---------------')
    print('----------------------------------')
    print('n\tx0\t\ty0\t\tslope\tyn')
    print('----------------------------------')
    for i in range(int(n)):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print(i,'\t%.3f\t%.3f\t%0.3f\t%.3f' % (x0, y0, slope, yn))
        print('----------------------------------')
        y0 = yn
        x0 = x0 + h

    print('At x=%.3f, y=%.3f' % (xn, yn))


# Euler method call
euler(x0, y0, xn, step)

# -----------------------------------------------

# # Consider a differential equation
# # dy / dx =(x + y + xy)
#
# def func(x, y):
#     fx = x +2*y
#     return (fx)
#
# # Driver Code
# # Initial Values
# x0 = 1
# y0 = 1
# h = 0.1
#
# # Value of x at which we need approximation
# x = 2
#
#
# # Function for euler formula
# def euler(x0, y, h, x):
#     temp = -0
#
#     # Iterating till the point at which we
#     # need approximation
#     while x0 < x:
#         temp = y
#         y = y + h * func(x0, y)
#         x0 = x0 + h
#
#     # Printing approximation
#     print("Approximate solution at x = ", x, " is ", "%.6f" % y)
#
#
# euler(x0, y0, h, x)
