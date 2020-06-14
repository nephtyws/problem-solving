# from acmicpc.net


if __name__ == '__main__':
    # TODO: 더 개선하는 방법 : colors 2칸만 번갈아가면서 쓰면 된다 (입력받으면서 동시에 계산하면 됨. 어차피 한 번 계산하는 순간 해당 결과에 이전 결과가 누적되기 때문에)
    # TODO: 또한, modular 연산이 비싸긴 하지만 쓰면 index를 좀 더 똑똑하게 써줄 수 있다

    number_of_house = int(input())
    colors = []

    DP = [[0] * 3 for _ in range(number_of_house)]

    for _ in range(number_of_house):
        colors.append(list(map(lambda x: int(x), input().split())))

    # 첫 번째 집을 칠하는 색칠 비용은 기본값으로 준다
    for i in range(3):
        DP[0][i] = colors[0][i]

    for i in range(1, number_of_house):
        DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + colors[i][0]
        DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + colors[i][1]
        DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + colors[i][2]

    print(min(DP[number_of_house - 1][0], DP[number_of_house - 1][1]), DP[number_of_house - 1][2])
