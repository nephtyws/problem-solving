/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <string>
#include <cstring>

using namespace std;

/* 3가지 방법이 있다.
1 : 내가 한 방법 (index 저장을 해놓으면 시간을 더 단축시킬 수 있음!)
2 : 배열로 하는 방법
3 : 내가 한 방법의 진보 (substring)
*/

int main()
{
	int quantity, length, count = 0;
	int alphabet[26] = { 0 };

	cin >> quantity;

	string* input = new string[quantity];

	for (int i = 0; i < quantity; i++)
		cin >> input[i];

	for (int i = 0; i < quantity; i++)
	{
		length = input[i].length();

		for (int j = 0; j < length; j++)
		{
			if (j == length - 1)
			{
				alphabet[input[i][j] - 'a']++;

				if (alphabet[input[i][j] - 'a'] == 2)
					break;

				else
					count++;
			}

			if (input[i][j] != input[i][j + 1])
				alphabet[input[i][j] - 'a']++;

			if (alphabet[input[i][j] - 'a'] == 2)
				break;
		}

		memset(alphabet, 0, sizeof(alphabet));
	}

	cout << count;
}
