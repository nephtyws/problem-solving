/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <string>

using namespace std;

int main()
{
	string input;
	int count = 0;
	bool tick = false;

	getline(cin, input);

	int length = input.length();

	for (int i = 0; i < length; i++)
	{
		if (tick && input[i] != 32)
			continue;

		else if (input[i] != 32)
		{
			tick = true;
		}

		else if (input[i] == 32)
		{
			if (tick)
				count++;

			tick = false;
		}
	}

	if (length == input.length() && tick)
		count++;

	if (length == 0)
		cout << 0;

	else
		cout << count;
}
