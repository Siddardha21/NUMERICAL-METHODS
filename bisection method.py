import sympy as sym
from sympy import *
x=symbols('x')
a=0
b=3
fx=2*x-5

for i in range(8):

    x_i=(a+b)/2

    value_a=fx.subs(x,a)
    value_b=fx.subs(x,b)
    value_x_i=fx.subs(x,x_i)
    print("a\t=",a,"\tb\t=",b,"\txi\t=",x_i)

    if value_a<0 and value_x_i<0:
        a=x_i

    else:
        b=x_i





