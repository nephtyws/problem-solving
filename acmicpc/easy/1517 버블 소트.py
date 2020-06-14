# from acmicpc.net


shuffle = 0


def merge(left, middle, right):
    global shuffle

    result = []

    left_length = len(left)
    right_length = len(right)
    i = j = 0

    while i < left_length and j < right_length:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        # i > j, A[i] < A[j] 인 개수 세기
        # merge 과정에서 오른쪽 배열에 있던 것이 주 배열로 들어갈 때 왼쪽 배열에 몇 개가 있는지 세면 됨
        else:
            result.append(right[j])
            j += 1
            shuffle += middle - i

    while i < left_length:
        result.append(left[i])
        i += 1

    while j < right_length:
        result.append(right[j])
        j += 1

    return result


def merge_sort(values):
    middle = len(values) // 2

    if middle < 1:
        return values

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, middle, right)


n = int(input())
numbers = [int(number) for number in input().split()]

merge_sort(numbers)
print(shuffle)
