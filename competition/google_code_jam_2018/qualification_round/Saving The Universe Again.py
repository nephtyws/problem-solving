# https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007966


test_case = int(input())

test_list = list()

for i in range(test_case):
    shield, instruction = input().split()
    test_list.append((i + 1, int(shield), instruction))

for i, shield, instruction in test_list:
    c_count = instruction.count('C')
    s_count = instruction.count('S')
    length = len(instruction)

    # Only C
    if c_count == length:
        answer = 0
        print("Case #%d: %s" % (i, answer))
        continue

    # Only S
    elif s_count == length:
        if s_count > shield:
            answer = 'IMPOSSIBLE'
            print("Case #%d: %s" % (i, answer))
            continue

        elif s_count <= shield:
            answer = 0
            print("Case #%d: %s" % (i, answer))
            continue

    # Contains both C and S
    else:
        strength = 1
        damage = 0
        count = 0

        for character in instruction:
            if character == 'S':
                damage += strength

            else:
                strength = strength << 1

        # Shield bear
        if damage <= shield:
            answer = 0
            print("Case #%d: %s" % (i, answer))
            continue

        # Calculate
        else:
            previous_instruction = None

            while True:
                strength = 1
                damage = 0

                failed = False
                count += 1
                previous_instruction = instruction
                reversed_instruction = instruction[::-1].replace('SC', 'CS', 1)
                instruction = reversed_instruction[::-1]

                if previous_instruction == instruction:
                    answer = 'IMPOSSIBLE'
                    print("Case #%d: %s" % (i, answer))
                    break

                for character in instruction:
                    if character == 'S':
                        damage += strength

                    else:
                        strength = strength << 1

                    # Failed
                    if damage > shield:
                        failed = True
                        break

                if not failed:
                    answer = count
                    print("Case #%d: %s" % (i, answer))
                    break
