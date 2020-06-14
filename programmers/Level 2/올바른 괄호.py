# https://programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    a = 0

    for i in s:
        if i == '(':
            a += 1

        else:
            a -= 1

        if a < 0:
            return False

    if a != 0:
        return False

    return True
