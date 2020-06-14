# from acmicpc.net, solved on 2016


list = list()

for i in range(1, 1000):
    temp = i
    while i > 0:
        list.append(temp)
        i -= 1

a, b = map(int, input().split())
sum = 0

for i in range(a - 1, b):
    sum += list[i]

print(sum)
