from sympy import Symbol, Derivative
import sympy as sym
import math
x = Symbol('x')

gx = x**3 - 4 # Giving G(x) function.
deriv = Derivative(gx, x)
dgx = deriv.doit()  # Derivative of G(x)
print("derivative of G(x)=",dgx)
value = 1/2
approx = float(dgx.subs({x:value}))  # Substituting the value in G'(x).
print("g'(x) =",approx)
for i in range(13):
    print('---------iteration',i+1,'-----------')
    ans = gx.subs({x:value})
    print("answer=",float(ans))
    value = ans
