# https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007a30


test_case = int(input())


for i in range(test_case):
    answer_tile = int(input())

    x = 999
    y = 999

    if answer_tile == 20:
        target_x = 1
        target_y = 5

        width, height = 7, 3
        answer_array = [[0 for x in range(width)] for y in range(height)]

        # Solving start
        for j in range(1000):
            # Send number
            print("%d %d" % (x, y), flush=True)

            read_x, read_y = map(int, input().split())

            if read_x == 0 and read_y == 0:
                break

            answer_array[read_x - 998][read_y - 994] = 1

            if target_y == 1:
                pass

            elif answer_array[target_x][target_y] == 1 and answer_array[target_x - 1][target_y] == 1 and answer_array[target_x + 1][target_y]:
                if target_y == 5:
                    if answer_array[target_x - 1][target_y + 1] != 1 or answer_array[target_x][target_y + 1] != 1 or answer_array[target_x + 1][target_y + 1] != 1:
                        target_y += 1
                        y += 1

                target_y -= 1
                y -= 1

    elif answer_tile == 200:
        target_x = 1
        target_y = 65

        width, height = 67, 3
        answer_array = [[0 for x in range(width)] for y in range(height)]

        # Solving start
        for j in range(1000):
            # Send number
            print("%d %d" % (x, y), flush=True)

            read_x, read_y = map(int, input().split())

            if read_x == 0 and read_y == 0:
                break

            answer_array[read_x - 998][read_y - 934] = 1

            if target_y == 1:
                pass

            elif answer_array[target_x][target_y] == 1 and answer_array[target_x - 1][target_y] == 1 and answer_array[target_x + 1][target_y]:
                if target_y == 65:
                    if answer_array[target_x - 1][target_y + 1] != 1 or answer_array[target_x][target_y + 1] != 1 or answer_array[target_x + 1][target_y + 1] != 1:
                        target_y += 1
                        y += 1

                target_y -= 1
                y -= 1
