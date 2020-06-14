/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int N;
	int A[50], B[50];
	int S = 0;

	cin >> N;

	for (int i = 0; i < N; i++)
		cin >> A[i];

	for (int j = 0; j < N; j++)
		cin >> B[j];

	sort(A, A + N, greater<int>());
	sort(B, B + N);

	for (int i = 0; i < N; i++)
		S += A[i] * B[i];

	cout << S;
}
