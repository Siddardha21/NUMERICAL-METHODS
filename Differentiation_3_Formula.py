from sympy import Symbol, Derivative
import sympy as sym
import math

x = Symbol('x')

# Given the Initial Conditions.

fx = x**3 - 6*x**2 + 11*x - 6

x_gvn = 0.5
h = 0.5

# ----------------------------------------------
x_plus_h = x_gvn + h
x_minus_h = x_gvn - h

# ---------------------------------------------
deriv = Derivative(fx, x)
dfx = deriv.doit()  # Derivative of F(x)
print("\nF'(x) =",dfx)

dfx_true_value = float(dfx.subs({x:x_gvn}))  # Substituting the value in F'(x).
print("True Value of F'(x) =",dfx_true_value)

fx_value = float(fx.subs({x:x_gvn}))  # f(x) value
print("\nF(x) = F(",x_gvn,") =",fx_value)

fx_plus_h = float(fx.subs({x:x_plus_h}))  # f(x+h) value
print("F(x+h) = F(",x_plus_h,") =",fx_plus_h)

fx_minus_h = float(fx.subs({x:x_minus_h}))  # f(x-h) value
print("F(x-h) = F(",x_minus_h,") =",fx_minus_h)

# 1st Order Differentiation -------------------------------------------------
fd_one = (fx_plus_h - fx_value)/h
print("\n1st Order Forward Diff = ",fd_one)
fe_one = (dfx_true_value - fd_one)/dfx_true_value*100
print("Forward Error = ",abs(fe_one),"%")

bd_one = (fx_value - fx_minus_h)/h
print("\n1st Order Backward Diff = ",bd_one)
be_one = (dfx_true_value - bd_one)/dfx_true_value*100
print("Backward Error = ",abs(be_one),"%")

cd_one = (fx_plus_h - fx_minus_h)/(2*h)
print("\n1st Order Centered Diff = ",cd_one)
ce_one = (dfx_true_value - cd_one)/dfx_true_value*100
print("Backward Error = ",abs(ce_one),"%")

# 2nd Order Differentiation ------------------------------------------------------
print('----------------------------------')
cd_two = (fx_plus_h - 2*fx_value + fx_minus_h)/(h**2)
print("2nd Order Centered Diff = ",cd_two)
# ce_two = (dfx_true_value - cd_two)/dfx_true_value*100
# print("Backward Error = ",abs(ce_two),"%")

# 3rd Order Differentiation ------------------------------------------------------
print('----------------------------------')
x_plus_2h = x_gvn + 2*h
x_minus_2h = x_gvn - 2*h
# -------------------
# fx_value = float(fx.subs({x:x_gvn}))  # f(x) value
print("F(x) = F(",x_gvn,") =",fx_value)

# fx_plus_h = float(fx.subs({x:x_plus_h}))  # f(x+h) value
print("F(x+h) = F(",x_plus_h,") =",fx_plus_h)

fx_minus_h = float(fx.subs({x:x_minus_h}))  # f(x-h) value
print("F(x-h) = F(",x_minus_h,") =",fx_minus_h)

fx_plus_2h = float(fx.subs({x:x_plus_2h}))  # f(x+2h) value
print("F(x+2h) = F(",x_plus_2h,") =",fx_plus_2h)

fx_minus_2h = float(fx.subs({x:x_minus_2h}))  # f(x-2h) value
print("F(x-2h) = F(",x_minus_2h,") =",fx_minus_2h)
# ---------------------

cd_three = (fx_plus_2h - 2*fx_plus_h + 2*fx_minus_h - fx_minus_2h)/(2*h**3)
print("---------\n3rd Order Centered Diff = ",cd_three)

# 4th Order Differentiation ------------------------------------------------------

cd_four = (fx_plus_2h - 4*fx_plus_h + 6*fx_value - 4*fx_minus_h + fx_minus_2h)/(h**4)
print("---------\n4th Order Centered Diff = ",cd_four)
