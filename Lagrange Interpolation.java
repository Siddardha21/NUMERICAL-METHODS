import java.util.*;

class GFG
{

// corresponding to x and y = f(x)
static class Data
{
    int x, y;

    public Data(int x, int y)
    {
        super();
        this.x = x;
        this.y = y;
    }

};

static double interpolate(Data f[], int xi, int n)
{
    double result = 0; // Initialize result

    for (int i = 0; i < n; i++)
    {
        // Compute individual terms of above formula
        double term = f[i].y;
        for (int j = 0; j < n; j++)
        {
            if (j != i)
                term = term*(xi - f[j].x) / (f[i].x - f[j].x);
        }

        // Add current term to result
        result += term;
    }

    return result;
}

public static void main(String[] args)
{
    // creating an array of 4 known data points
    Data f[] = {new Data(0, 2), new Data(1, 3), new Data(2, 12), new Data(5, 147)}; // manual input


    // a data point corresponding to x=3
    System.out.print("Value of f(3) is : " + (int)interpolate(f, 3, 4)); // manual input
}
}
