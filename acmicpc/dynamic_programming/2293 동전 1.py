# from acmicpc.net


if __name__ == '__main__':
    # 동전 종류 수, 가치의 합
    N, K = list(map(lambda x: int(x), input().split()))
    coins = []

    DP = [0] * 10001
    # 동전을 가지고 0원을 만드는 경우의 수
    DP[0] = 1

    # 동전 종류 수만큼 입력
    for _ in range(N):
        coins.append(int(input()))

    # TODO: 더 개선하는 방법 - if문은 for문 range를 적절히 주는 것으로 없앨 수 있다.

    for i in range(N):
        for j in range(1, K + 1):
            if j - coins[i] >= 0:
                DP[j] += DP[j - coins[i]]

    print(DP[K])
