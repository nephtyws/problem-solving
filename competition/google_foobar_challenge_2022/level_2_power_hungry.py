def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    answer = 0
    number_of_negative_panels = 0
    minimum_negative_panel = -9999
    zero_count = 0

    for i in range(len(xs)):
        if xs[i] == 0:
            zero_count += 1
            continue
        elif xs[i] < 0:
            number_of_negative_panels += 1
            if minimum_negative_panel < xs[i]:
                minimum_negative_panel = xs[i]

        if answer == 0:
            answer = xs[i]
        else:
            answer *= xs[i]

    if zero_count + 1 == len(xs) and number_of_negative_panels == 1:
        answer = 0
    elif number_of_negative_panels % 2 == 1:
        answer //= minimum_negative_panel

    return str(answer)
