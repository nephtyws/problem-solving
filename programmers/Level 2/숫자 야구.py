# https://programmers.co.kr/learn/courses/30/lessons/42841


from itertools import permutations


def possible(question, candidate, strike, ball):
    possible_strike = 0

    for q, c in zip(question, candidate):
        if q == c:
            possible_strike += 1

    if possible_strike != strike:
        return False

    possible_ball = len(set(question) & set(candidate)) - strike

    if possible_ball != ball:
        return False

    return True


def solution(baseball):
    candidates = list(permutations([i for i in range(1, 10)], 3))

    for numbers, strike, ball in baseball:
        for candidate in candidates[:]:
            if not possible([int(number) for number in str(numbers)],
                            candidate,
                            strike,
                            ball):
                candidates.remove(candidate)

    return len(candidates)
