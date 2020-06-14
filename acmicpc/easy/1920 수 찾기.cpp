/* from acmicpc.net, solved on 2015 */


#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int compare(const void* a, const void* b)
{
	if (*(int *)a < *(int *)b)
		return -1;

	else if (*(int *)a == *(int *)b)
		return 0;

	else
		return 1;

	// 0이면 현재 가리키고 있는 놈이랑 같다.
	// 1, -1이면 앞에 있다 / 뒤에 있다.
	// 그러므로 return 0했을 때 bsearch에서 받아들이는 건 0(가리키고 있는 놈이랑 같다) 이니까,
	// 최종적인 bsearch의 return value는 key(가리키고 있는 놈) 이다.
	// 여기서 양수 or 음수이므로.. 근데 0일 때는?
	// 0일 때 이게 false가 아닌 이유는 void* type 이라서.
}

int main()
{
	int N, M;

	cin >> N;

	int* A = new int[N];

	for (int i = 0; i < N; i++)
		cin >> A[i];

	cin >> M;

	int* B = new int[M];

	sort(A, A + N);

	for (int i = 0; i < M; i++)
		cin >> B[i];

	for (int i = 0; i < M; i++)
		if (bsearch(&B[i], A, N, sizeof(int), compare))
			printf("1\n");

		else
			printf("0\n");
}
