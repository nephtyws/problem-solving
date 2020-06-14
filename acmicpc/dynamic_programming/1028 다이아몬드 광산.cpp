/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <string>

using namespace std;

int main()
{
	int r, c;

	cin >> r >> c;

	char** arr = new char*[r];
	int min = r <= c ? r : c;

	if (min % 2 == 0)
		min /= 2;

	else
		min = min / 2 + 1;

	min -= 1;

	for (int i = 0; i < r; i++)
	{
		arr[i] = new char[c];

		for (int j = 0; j < c; j++)
			cin >> arr[i][j];
	}

	for (; min >= 1; min--)
	{
		for (int i = 0; i < r; i++)
		{
			if (i + min * 2 >= r)
				continue;

			for (int j = 0; j < c; j++)
			{
				if (j + min * 2 >= c)
					continue;

				for (int k = 0; k < min * 2 + 1; k++)
				{
					if (k <= min)
					{
						if (arr[i + k][j + min - k] == '0' || arr[i + k][j + min + k] == '0')
							break;
					}

					if (k > min && k < min * 2)
					{
						if (arr[i + k][j - min + k] == '0' || arr[i + k][j + (3 * min) - k] == '0')
							break;
					}

					if (k == min * 2)
					{
						if (arr[i + k][j - min + k] == '1')
						{
							cout << min + 1;
							return 0;
						}
					}
				}
			}
		}
	}

	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			if (arr[i][j] == '1')
			{
				cout << 1;
				return 0;
			}
		}

	cout << 0;
	return 0;
}
