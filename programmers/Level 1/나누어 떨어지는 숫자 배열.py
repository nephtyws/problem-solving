# https://programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    result = []

    for i in arr:
        if i % divisor == 0:
            result.append(i)

    if len(result) == 0:
        return [-1]

    return sorted(result)
