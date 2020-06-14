# 에라토스테네스의 체


def solution(n):
    sieve = [0, 0] + [1] * (n - 1)
    answer = 0

    for i in range(2, n + 1):
        if sieve[i]:
            answer += 1

            for j in range(2 * i, n + 1, i):
                sieve[j] = 0

    return answer
