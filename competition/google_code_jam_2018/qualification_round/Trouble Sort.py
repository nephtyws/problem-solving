# https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cb
# Failed on second test case


test_case = int(input())

test_case_list = list()

for i in range(test_case):
    list_length = int(input())

    test_case_list.append((input().split()))

    test_case_list[i] = list(map(int, test_case_list[i]))

for count, test_numbers in enumerate(test_case_list):
    while True:
        swapped = False

        for i in range(0, len(test_numbers) - 2):
            if test_numbers[i] > test_numbers[i + 2]:
                temp = test_numbers[i + 2]
                test_numbers[i + 2] = test_numbers[i]
                test_numbers[i] = temp

                swapped = True

        if not swapped:
            break

    failed = False

    for i in range(0, len(test_numbers) - 1):
        if test_numbers[i] > test_numbers[i + 1]:
            print("Case #%d: %d" % (count + 1, i))
            failed = True
            break

    if not failed:
        print("Case #%d: OK" % (count + 1))
