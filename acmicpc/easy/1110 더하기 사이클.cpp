/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <string>

using namespace std;

// 10보다 작으면 앞에 0 붙이기?

int main()
{
	char input[3];

	cin >> input;

	if (input[1] == NULL)
	{
		input[1] = input[0];
		input[0] = '0';
	}

	int answer = atoi(input);
	char init[3];
	init[0] = input[1];
	init[1] = ((input[0] - '0') + (input[1] - '0')) + '0';

	if (init[1] > '9')
	{
		int correct = (init[1] - '0') - 10;
		init[1] = correct + '0';
	}

	int count = 1;

	while (atoi(init) != answer)
	{
		char next[3];
		next[0] = init[1];
		next[1] = ((init[0] - '0') + (init[1] - '0')) + '0';

		if (next[1] > '9')
		{
			int correct = (next[1] - '0') - 10;
			next[1] = correct + '0';
		}

		count++;

		init[0] = next[0];
		init[1] = next[1];
	}

	cout << count << endl;
}
