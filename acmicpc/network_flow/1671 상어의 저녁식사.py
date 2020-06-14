# from acmicpc.net


import queue as Queue


class Shark:
    def __init__(self, size, speed, intel):
        self.size = size
        self.speed = speed
        self.intel = intel


def set_edge(start, dest, weight):
    edges[start].append(dest)
    edges[dest].append(start)
    flow[start][dest] += weight


if __name__ == "__main__":
    number_of_sharks = int(input())

    # TODO: 개선할 점 - 공간을 좀 더 절약하면서 할 수 있는 방법이 있을 것이다.
    # e.g.) 지나간 길에 대한 정보..? 절약?

    # +2 : add source and sink
    number_of_networks = number_of_sharks * 2 + 2
    SOURCE = number_of_sharks * 2
    SINK = number_of_sharks * 2 + 1

    sharks = []
    edges = [[] for _ in range(number_of_networks)]
    flow = [[0] * number_of_networks for _ in range(number_of_networks)]

    for i in range(number_of_sharks):
        size, speed, intel = list(map(lambda x: int(x), input().split()))
        sharks.append(Shark(size, speed, intel))

    for i in range(number_of_sharks):
        # source to A group (predator)
        set_edge(SOURCE, i * 2, 2)
        # B group to sink (prey)
        set_edge(i * 2 + 1, SINK, 1)

        for j in range(len(sharks)):
            if i == j:
                continue

            if sharks[i].size == sharks[j].size and sharks[i].speed == sharks[j].speed and sharks[i].intel == sharks[j].intel and i > j:
                continue

            if sharks[i].size >= sharks[j].size and sharks[i].speed >= sharks[j].speed and sharks[i].intel >= sharks[j].intel:
                set_edge(i * 2, j * 2 + 1, 1)

    answer = len(sharks)

    while True:
        visited = [-1 for _ in range(number_of_networks)]
        queue = Queue.Queue(number_of_networks)
        queue.put(SOURCE)

        while not queue.empty() and visited[SINK] == -1:
            u = queue.get()

            for v in edges[u]:
                if flow[u][v] > 0 and visited[v] == -1:
                    queue.put(v)
                    visited[v] = u

        if visited[SINK] == -1:
            break

        u = SINK
        while u != SOURCE:
            flow[visited[u]][u] -= 1
            flow[u][visited[u]] += 1
            u = visited[u]

        answer -= 1

    print(answer)
