def solution(x, y):
    x, y = max(int(x), int(y)), min(int(x), int(y))
    counter = 0

    while y > 0:
        counter += x // y
        x, y = y, x % y

    if x != 1:
        return "impossible"

    return str(counter - 1)
