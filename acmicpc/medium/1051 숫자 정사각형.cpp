/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n, m;

	cin >> n >> m;

	string* s = new string[n];
	int** arr = new int*[n];
	int min = n <= m ? n : m;

	for (int i = 0; i < n; i++)
	{
		cin >> s[i];
		arr[i] = new int[m];

		for (int j = 0; j < m; j++)
			arr[i][j] = s[i][j] - '0';
	}

	for (; min > 1; min--) // 3x3 -> 2x2 -> 1x1 (안 봄. 점이라서) 정사각형을 검사
	{
		for (int i = 0; i < n; i++) // 세로로 검사 (n)
		{
			if (i + min - 1 >= n) // 3x5 인데 4x5 자리로 갔을 경우를 방지 (세로)
				continue;

			for (int j = 0; j < m; j++) // 가로로 검사 (m)
			{
				if (j + min - 1 >= m) // 3x5 인데 3x6 자리로 갔을 경우를 방지 (가로)
					continue;

				if ((arr[i][j] == arr[i][j + min - 1]) &&
					(arr[i][j] == arr[i + min - 1][j]) &&
					(arr[i][j] == arr[i + min - 1][j + min - 1]))
				{
					cout << min * min;
					return 0;
				}
			}
		}
	}

    cout << 1;
}
