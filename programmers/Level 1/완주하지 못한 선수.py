# https://programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    participant_dict = {}

    for runner in participant:
        participant_dict[runner] = participant_dict.get(runner, 0) + 1

    for runner in completion:
        if runner not in participant_dict:
            return runner

        else:
            participant_dict[runner] -= 1

    for key in participant_dict:
        if participant_dict[key] != 0:
            return key
