# MULLER METHOD
import sympy as sym
from sympy import Symbol, Derivative
print("\t---Muller Method---")
x = Symbol('x')
x0 = 4.5
x1 = 5.5
x2 = 5
fx = x**3-13*x-12  # Give the Function.

fx0=fx.subs({x:x0})
print("F(x0)=",fx0)
fx1=fx.subs({x:x1})
print("F(x1)=",fx1)
fx2=fx.subs({x:x2})
print("F(x2)=",fx2)

h0 = x1 - x0
print("\nh0=",h0)
h1 = x2 - x1
print("h1=",h1)

d0 = (fx1 - fx0)/h0
print("Delta 0=",d0)
d1 = (fx2 - fx1)/h1
print("Delta 1=",d1)

a = (d1 - d0)/(h1 +h0)
print("\na=",a)
b = a*h1 + d1
print("b=",b)
c = fx2
print("c=",c)

x3 = x2 + -(2*c)/(b+(b*2 - 4*a*c)*(1/2))
print("\nx3=",x3)
e = ((x3-x2)*100)/x3
print("Error= %.2f"%abs(e),"%")
