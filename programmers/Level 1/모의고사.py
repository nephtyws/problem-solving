# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = [[0, i] for i in range(3)]
    result = []

    for i, ans in enumerate(answers):
        for j in range(3):
            if pattern[j][i % len(pattern[j])] == ans:
                answer[j][0] += 1

    answer = sorted(answer, key=lambda x: x[0], reverse=True)
    max = 0

    for ans in answer:
        if ans[0] >= max:
            result.append(ans[1] + 1)
            max = ans[0]

        else:
            break

    return result
