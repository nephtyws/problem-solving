# from acmicpc.net, solved on 2016


string = input()

upper = list()
upper.append(string[0])

for i in range(len(string)):
    if string[i] == '-':
        if string[i + 1].isupper():
            upper.append(string[i + 1])

print(''.join(upper))
