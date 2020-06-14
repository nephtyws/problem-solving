/* from acmicpc.net, solved on 2015 */


#include <iostream>

using namespace std;

int main()
{
    int input;
    int temp = 1;

    cin >> input;

    int e = 1;

    while (input > temp)
    {
        temp += 6 * e;
        e++;
    }

    cout << e;
}
