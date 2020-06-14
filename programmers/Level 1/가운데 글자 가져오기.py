# https://programmers.co.kr/learn/courses/30/lessons/12903


def solution(s):
    middle_length = int(len(s) / 2)

    if len(s) % 2 == 0:
        return s[middle_length - 1:middle_length + 1]

    else:
        return s[middle_length:middle_length + 1]
