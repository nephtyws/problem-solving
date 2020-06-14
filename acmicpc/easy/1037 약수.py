# from acmicpc.net, solved on 2016


tries = int(input())
line = input()

x = line.split(' ')
x = list(map(int, x))
x.sort()
print(int(x[0]) * int(x[len(x) - 1]))
