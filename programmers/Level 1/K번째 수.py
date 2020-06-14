# https://programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answers = []
    for command in commands:
        command[0] -= 1
        if command[0] == command[1]:
            command[1] += 1

        answers.append(sorted(array[command[0]:command[1]])[command[2] - 1])

    return answers
