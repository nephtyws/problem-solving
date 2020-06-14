/* from acmicpc.net, solved on 2015 */


#include <iostream>

using namespace std;

double fac(double n) {
    double ans = 1;
    for (int i = 1; i <= n; i++)
        ans *= i;
    return ans;
}

int main() {
    bool flag = true;
    int end;
    int num;

        cin >> num;

    double* mm = new double[num];
    double* nn = new double[num];

    for (int i = 0; i < num; i++) {
        cin >> nn[i];
        cin >> mm[i];
    }

    for (int i = 0; i < num; i++)
        printf("%.0lf\n", (fac(mm[i]) / (fac(nn[i]) * fac(mm[i] - nn[i]))));
}

