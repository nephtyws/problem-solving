# from acmicpc.net


DP = [-1] * 91


def pinary_number(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    elif DP[n] != -1:
        return DP[n]

    else:
        DP[n] = pinary_number(n - 1) + pinary_number(n - 2)
        return DP[n]


if __name__ == '__main__':
    # N자리 이친수
    N = int(input())

    print(pinary_number(N))
