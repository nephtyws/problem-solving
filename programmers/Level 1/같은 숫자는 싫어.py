# https://programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i + 1 == len(arr):
            answer.append(arr[i])
            break

        if arr[i] == arr[i + 1]:
            continue

        answer.append(arr[i])

    return answer
