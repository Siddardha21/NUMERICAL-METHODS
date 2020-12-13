import sympy as sym
import numpy as np
import math
import scipy.integrate as integrate

fun = lambda x : x*sym.exp(x)  # Function Input------@@@
a = -1
b = 0.5

I = integrate.quad(fun,a,b)

print ('\nThe approximate value = %f' % (I[0]))
# -------------------------------------------------------

from scipy import integrate

fx = lambda t: 1/(1+t**2)  # Function Input -------@@@
low = 2.2
high = 0.2
# using scipy.integrate.quadrature() method
gauss = integrate.quadrature(fx, low, high)

print("---------\nGauss Answer is ",gauss)

# --------------------------------------------------------
# 2 and 3 point Values..
from sympy import Symbol
q = Symbol('q')
function = q*sym.exp(q)  # Function Input -----@@@

gqi_2 = float(function.subs({q: 0.2})) + float(function.subs({q: 2.2}))
print("---------\n2 point F(x) =",gqi_2)

f1=float(function.subs({q:-(3/5)**(1/2)}))
f2=float(function.subs({q:0}))
f3=float(function.subs({q:(3/5)**(1/2)}))

gqi_3 = (5/9)*f1 + (8/9)*f2 + (5/9)*f3
print("---------\n3 point F(x) =",gqi_3)

