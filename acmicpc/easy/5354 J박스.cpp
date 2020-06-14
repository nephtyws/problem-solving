/* from acmicpc.net, solved on 2015 */


#include <iostream>

using namespace std;

int main()
{
    int n;
    int temp;
    cin >> n;

    int* arr = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i++)
    {
        temp = arr[i];

        if (temp == 1)
        {
            cout << "#" << endl << endl;
            continue;
        }

        for (int e = 0; e < temp; e++)
        {
            cout << "#";

            for (int j = 0; j < temp - 2; j++)
            {
                if (e == 0)
                    cout << "#";

                else if (e == temp - 1)
                    cout << "#";

                else
                    cout << "J";
            }

            cout << "#" << endl;
        }

        cout << endl;
    }
}
