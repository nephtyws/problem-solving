# https://programmers.co.kr/learn/courses/30/lessons/12922


def solution(n):
    answer = "수박" * int((n + 1) / 2)

    if n % 2 == 1:
        answer = answer[:-1]

    return answer