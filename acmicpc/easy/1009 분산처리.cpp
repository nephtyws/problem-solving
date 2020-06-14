/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T;
	int a, b;
	int mod;

	int list[10][4] = { {},{ 1 },{ 6, 2, 4, 8 },{ 1, 3, 9, 7 },{ 6,4 },{ 5 },{ 6 },{ 1, 7, 9, 3 },{ 6, 8, 4, 2 },{ 1,9 } };

	cin >> T;

	int* answer = new int[T];

	for (int i = 0; i < T; i++)
	{
		cin >> a >> b;

		a = a % 10;

		if (a == 1 || a == 5 || a == 6)
			answer[i] = a;

		else if (a == 2 || a == 3 || a == 7 || a == 8)
		{
			mod = b % 4;
			answer[i] = list[a][mod];
		}

		else if (a == 4 || a == 9)
		{
			mod = b % 2;
			answer[i] = list[a][mod];
		}

		else if (a == 0)
			answer[i] = 10;
	}

	for (int i = 0; i < T; i++)
		printf("%d\n", answer[i]);
}
