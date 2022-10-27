def solution(x):
    ASCII_LOWER_A = ord("a")
    ASCII_LOWER_Z = ord("z")
    answer = []

    for alphabet in x:
        if ASCII_LOWER_A <= ord(alphabet) <= ASCII_LOWER_Z:
            answer.append(chr(ASCII_LOWER_Z - ord(alphabet) + ASCII_LOWER_A))

        else:
            answer.append(alphabet)

    return "".join(answer)
