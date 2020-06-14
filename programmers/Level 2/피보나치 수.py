# https://programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    memoization = {0: 0, 1: 1, 2: 1}

    for i in range(3, n + 1):
        memoization[i] = memoization[i - 1] + memoization[i - 2]

    return memoization[n] % 1234567
