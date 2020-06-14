/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <string>

using namespace std;

int main()
{
	int N;

	cin >> N;

	string* S = new string[N];
	string C;
	int length;
	bool diff = false;

	for (int i = 0; i < N; i++)
		cin >> S[i];

	length = S[0].length();
	int tempIndex = 0;

	for (int i = 0; i < length; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (j + 1 != N)
			{
				if (S[j][i] != S[j + 1][i])
				{
					C += "?";
					diff = true;
					break;
				}
			}

			else
				continue;

			tempIndex = j;
		}

		if (!diff)
			C += S[tempIndex][i];

		else
			diff = false;
	}

	cout << C;
}
