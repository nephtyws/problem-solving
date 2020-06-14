# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # if phone_book[i] in phone_book[i + 1]:
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


# Another answer
def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x), reverse=True)
    prefixes = {}

    for number in phone_book:
        if number not in prefixes:
            for i in range(1, len(number) + 1):
                prefixes[number[0:i]] = True

        else:
            return False

    return True
