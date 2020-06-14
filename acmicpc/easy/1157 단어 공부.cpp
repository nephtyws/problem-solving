/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <string>

using namespace std;

int main()
{
	int alphabet[26] = { 0 };
	string input;
	int max = 0;
	int index = 0;
	int length;

	cin >> input;

	length = input.length();

	for (int i = 0; i < length; i++)
	{
			input[i] = tolower(input[i]);

		alphabet[input[i] - 'a']++;
	}

	for (int i = 0; i < 26; i++)
	{
		if (max < alphabet[i])
		{
			max = alphabet[i];
			index = i;
		}
	}

	for (int i = 0; i < 26; i++)
	{
		if (max == alphabet[i])
		{
			if (i == index)
				continue;

			printf("?");
			return 0;
		}
	}

	printf("%c", (index + 'A'));
}
