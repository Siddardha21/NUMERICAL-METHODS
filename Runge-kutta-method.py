
# function to be solved
def f(x, y):
	fx = x+y		# Function Input ---------
	return fx
	# or fx = lambda x,y: x+y


# Inputs
x0 = 0
y0 = 1
xn = 1
step = 2
# RK-4 method


def rk4(x0, y0, xn, n):
	# Calculating step size
	h = (xn - x0) / n

	print('\n\t\t\t\tRK METHOD SOLUTION')
	print('-------------------------------------------------------')
	print('k1\t\tk2\t\tk3\t\tk4\t\tx0\t\ty0\t\tyn')
	print('-------------------------------------------------------')
	for i in range(int(n)):
		k1 = h * (f(x0, y0))
		k2 = h * (f((x0 + h / 2), (y0 + k1 / 2)))
		k3 = h * (f((x0 + h / 2), (y0 + k2 / 2)))
		k4 = h * (f((x0 + h), (y0 + k3)))
		k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
		yn = y0 + k
		print('%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f' % (k1,k2,k3,k4,x0, y0, yn))
		print('-------------------------------------------------------')
		y0 = yn
		x0 = x0 + h

	print('\nAt x = %.4f, y = %.4f' % (xn,yn))

# -----------------------------------------------------------------------------------------------
# RK4 method call
rk4(x0, y0, xn, step)

# # Python program to implement Runge Kutta method
# # A sample differential equation "dy / dx = (x - y)/2"
# def dydx(x, y):
# 	fx = (y+x)**0.5
# 	return (fx)
#
#
# # Driver method
# x0 = 0.4
# y = 0.41
# h = 0.1
# # At what value of x
# x = 0.8
#
# # Finds value of y for a given x using step size h and initial value y0 at x0.
# def rungeKutta(x0, y0, x, h):
# 	# Count number of iterations using step size or
# 	# step height h
# 	n = (int)((x - x0)/h)
# 	# Iterate for number of iterations
# 	y = y0
# 	for i in range(1, n + 1):
# 		"Apply Runge Kutta Formulas to find next value of y"
# 		k1 = h * dydx(x0, y)
# 		k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
# 		k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
# 		k4 = h * dydx(x0 + h, y + k3)
# 		print("\nk1=%.4f \nk2=%.4f \nk3=%.4f \nk4=%.4f" % (k1, k2, k3, k4))
# 		# Update next value of y
# 		y = y + (1 / 6)*(k1 + 2 * k2 + 2 * k3 + k4)
#
# 		# Update next value of x
# 		x0 = x0 + h
# 	return y
#
#
# print('\nAt x =',x,',Y =%.5f' % rungeKutta(x0, y, x, h))
