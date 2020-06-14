/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double x1, y1, x2, y2, a, b;
    double X, Y;

    cin >> x2 >> y2;

    cin >> x1 >> y1 >> a >> b;

    if (a == 0 && b == 0)
    {
	    X = x1;
	    Y = y1;
    }

    else if (b == 0)
    {
	    X = x2;
	    Y = y1;
    }

    else if (a == 0)
    {
	    X = x1;
	    Y = y2;
    }

    else
    {
        X = ((a * b) / (pow(a, 2) + pow(b, 2))) * ((b / a * x1) + (a / b * x2) + y2 - y1);
        Y = ((b / a) * (X - x1)) + y1;

        if (X < x1)
        {
            X = x1;
            Y = y1;
        }
    }

  cout << X << " " << Y;
}
