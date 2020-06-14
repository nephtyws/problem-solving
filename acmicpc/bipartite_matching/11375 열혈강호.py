# from acmicpc.net


def traverse(a: int):
    if visited[a]:
        return False

    visited[a] = True

    for b in range(len(match_list[a])):
        if match_list[a][b]:
            if not matched_work[b] or traverse(matched_work[b]):
                matched_employee[a] = b
                matched_work[b] = a
                return True

    return False


if __name__ == "__main__":
    employee, work = list(map(lambda x: int(x), input().split()))
    work_list = [[] for _ in range(employee)]

    for i in range(employee):
        work_list[i] = list(map(lambda x: int(x) - 1, input().split()))[1:]

    match_list = [[0] * max(employee, work) for _ in range(max(employee, work))]

    for i in range(len(work_list)):
        for job in work_list[i]:
            match_list[i][job] = True

    matched_employee = [False for _ in range(employee)]
    matched_work = [False for _ in range(work)]
    answer = 0

    for i in range(employee):
        visited = [False for _ in range(employee)]

        if traverse(i):
            answer += 1

    print(answer)
