import math
# BISECTION METHOD

print('\tBISECTION METHOD')
a=0
b=3
for i in range(8):
    print('------------Iteration',i+1,'--------------------------')
    print()
    print('a= ', a)
    print('b= ', b)
    x = (a + b) / 2
    print('x= ', x)
    fa = 2*a - 5# Give the function here.
    print('fa= ', fa)
    fb = 2*b - 5# Give the function here.
    print('fb= ', fb)
    fx = 2*x - 5# Give the function here.
    print('fx= ', fx)
    print()
    if (fa < 0 and fx < 0) or (fa > 0 and fx > 0):
        a = x
    else:
        b = x
