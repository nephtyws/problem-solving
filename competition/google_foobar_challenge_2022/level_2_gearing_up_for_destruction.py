def validate(pegs, radius):
    for i in range(1, len(pegs)):
        if radius < 1:
            return False

        radius = pegs[i] - (pegs[i - 1] + radius)

    return True


def solution(pegs):
    radius_of_first_gear = 0

    for i in range(len(pegs)):
        radius = (pegs[i] * ((-1) ** (i + 1)))
        if 0 < i < len(pegs) - 1:
            radius *= 2

        radius_of_first_gear += radius

    radius_of_first_gear *= 2
    denominator = 1

    if len(pegs) % 2 == 0:
        if radius_of_first_gear % 3 == 0:
            radius_of_first_gear /= 3
        else:
            denominator = 3

    if not validate(pegs, radius_of_first_gear / denominator):
        return [-1, -1]

    return [radius_of_first_gear, denominator]
