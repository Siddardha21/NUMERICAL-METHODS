# Simpson's rule
import math
import sympy

def func(x):
    fx = 1 / (1 + x * x)
    return float(fx)


# driver function

lower_limit = 0
upper_limit = 1
interval_limit = 6


# Function to perform calculations
def calculate(lower_limit, upper_limit, interval_limit):
    interval_size = (float(upper_limit - lower_limit) / interval_limit)
    sum = func(lower_limit) + func(upper_limit);

    # Calculates value till integral limit
    for i in range(1, interval_limit):
        if (i % 3 == 0):
            sum = sum + 2 * func(lower_limit + i * interval_size)
        else:
            sum = sum + 3 * func(lower_limit + i * interval_size)

    return ((float(3 * interval_size) / 8) * sum)



integral_res = calculate(lower_limit, upper_limit, interval_limit)

# rounding the final answer to 6 decimal places
print(round(integral_res, 4))