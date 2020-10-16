def proterm(i, value, x):
	pro = 1;
	for j in range(i):
		pro = pro * (value - x[j]);
	return pro;

def dividedDiffTable(x, y, n):

	for i in range(1, n):
		for j in range(n - i):
			y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
									(x[j] - x[i + j]));
	return y;
def applyFormula(value, x, y, n):

	sum = y[0][0];

	for i in range(1, n):
		sum = sum + (proterm(i, value, x) * y[0][i]);

	return sum;

def printDiffTable(y, n):

	for i in range(n):
		for j in range(n - i):
			print(round(y[i][j], 4), "\t",
							end = " ");

		print("");

n = 5; # manual input
y = [[0 for i in range(10)]
		for j in range(10)];
x = [ -1, 0, 3, 6, 7 ]; # manual input

y[0][0] = 3;  #  manual input
y[1][0] = -6;
y[2][0] = 39;
y[3][0] = 822;
y[4][0] = 1611;


y=dividedDiffTable(x, y, n);

printDiffTable(y, n);

# value to be interpolated
value = 2;

# printing the value
print("\nValue at", value, "is",
		round(applyFormula(value, x, y, n), 2))
