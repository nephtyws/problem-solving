# https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cc
# Failed on second test case


import math

test_case = int(input())

test_case_list = list()

for i in range(test_case):
    input_number = input()

    test_case_list.append(float(input_number))

for i, number in enumerate(test_case_list):
    if number <= 1.414213:
        theta = math.asin(number * number - 1.0) / 2.0
        pi = 0

    else:
        theta = math.pi / 4
        pi = math.asin(number - math.sqrt(2) - 1)

    print("Case #%d:" % (i + 1))
    print("%lf %lf %lf" % (math.cos(theta) * 0.5, 0.5 * math.sin(theta) * math.cos(pi), -0.5 * math.sin(theta) * math.sin(pi)))
    print("%lf %lf %lf" % (-0.5 * math.sin(theta), 0.5 * math.cos(theta) * math.cos(pi), -0.5 * math.cos(theta) * math.sin(pi)))
    print("%lf %lf %lf" % (0, 0.5 * math.sin(pi), 0.5 * math.cos(pi)))
