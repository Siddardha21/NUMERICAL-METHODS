# To represent a data point corresponding to x and y = f(x)
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def interpolate(f: list, xi: int, n: int) -> float:

    result = 0.0
    for i in range(n):

        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)

        # Add current term to result
        result += term

    return result

if __name__ == "__main__":

    # creating an array of 4 known data points
    f = [Data(0, 2), Data(1, 3), Data(2, 12), Data(5, 147)] # manual input


    # corresponding to x=3
    print("Value of f(3) is :", interpolate(f, 3, 4)) # manual input
