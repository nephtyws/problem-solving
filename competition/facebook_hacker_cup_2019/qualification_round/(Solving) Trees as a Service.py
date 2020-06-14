# https://www.facebook.com/hackercup/problem/330920680938986/


answer = []


def trees_as_a_service(tree, nodes, index):
    global answer
    duplicate = False

    # Check cycle
    # for i, node in enumerate(tree)

    print(tree, index)

    while index < len(nodes):
        print("while")
        tree[nodes[index][0] - 1][nodes[index][2] - 1] = 1
        tree[nodes[index][1] - 1][nodes[index][2] - 1] = 1
        index += 1

        # Slow
        for i, node in enumerate(tree):
            duplicate_rows = [j for j, x in enumerate(node) if x == 1]
            print(duplicate_rows)

            if len(duplicate_rows) >= 2:
                tree[i][duplicate_rows[0]] = 0
                trees_as_a_service(tree[:], nodes, index)

                tree[i][duplicate_rows[0]] = 1
                tree[i][duplicate_rows[1]] = 0
                trees_as_a_service(tree[:], nodes, index)

                duplicate = True
                break
        # Slow

    if not duplicate:
        answer.append(tree)

    return 0


test_case = int(input())

for i in range(test_case):
    size, number_of_nodes = list(map(lambda x: int(x), input().split()))
    tree = [[0] * size for _ in range(size)]
    nodes = []

    for _ in range(number_of_nodes):
        nodes.append(list(map(lambda x: int(x), input().split())))

    trees_as_a_service(tree, nodes, 0)
    print(f"Case #{i + 1}: ", end='')

    if all(tree is None for tree in answer):
        print("Impossible", end='')

    else:
        # Fetch the first answer
        for node in answer[0]:
            try:
                print(node.index(1) + 1, end=' ')

            except ValueError:
                print(0, end=' ')

    print()
