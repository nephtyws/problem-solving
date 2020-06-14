# from acmicpc.net, solved on 2016


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


tries = int(input())
a = list()
b = list()

for i in range(0, tries):
    t1, t2 = map(int, input().split())
    a.append(t1)
    b.append(t2)

for i in range(0, tries):
    temp = gcd(a[i], b[i])
    result = (a[i] * b[i]) // temp
    print(result)
