# https://programmers.co.kr/learn/courses/30/lessons/12899


def solution(n):
    answer = ""
    digits = ["4", "1", "2"]

    while n > 0:
        remainder = n % 3
        n //= 3

        if remainder == 0:
            n -= 1

        answer = digits[remainder] + answer

    return answer
