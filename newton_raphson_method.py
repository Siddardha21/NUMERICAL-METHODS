import sympy as sym
from sympy import *
x=symbols('x')

#sym.diff(x**3)
guess=1
fx=x**3+x-1
ffx=sym.diff(fx)
#print(fx.subs(x,2))

for i in range(8):
    value=fx.subs(x,guess)
    value1=ffx.subs(x,guess)
    z=guess-float(value/value1)
    print(z)
    guess=z
