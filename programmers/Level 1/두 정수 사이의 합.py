# https://programmers.co.kr/learn/courses/30/lessons/12912


def solution(a, b):
    if a == b:
        return a

    answer = 0

    for i in range(min(a, b), max(a, b) + 1):
        answer += i

    return answer
