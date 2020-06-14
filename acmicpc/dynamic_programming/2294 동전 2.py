# from acmicpc.net


if __name__ == '__main__':
    # 동전 종류 수, 가치의 합
    N, K = list(map(lambda x: int(x), input().split()))
    coins = []

    # 불가능한 값으로 설정
    DP = [10001] * 10001
    # 동전을 가지고 0원을 만드는 경우의 수
    DP[0] = 0

    # 동전 종류 수만큼 입력
    for i in range(N):
        coins.append(int(input()))

        # 비교 : 현재 상태를 그대로 사용하기 vs j - coins[i] 인 상태에서 현재 동전 더하기
        for j in range(coins[i], K + 1):
            DP[j] = min(DP[j], DP[j - coins[i]] + 1)

    if DP[K] != 10001:
        print(DP[K])

    else:
        print(-1)
