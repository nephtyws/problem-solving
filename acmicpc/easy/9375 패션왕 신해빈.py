import functools


test_cases = int(input())
closet = {}

for _ in range(test_cases):
    number_of_cloth = int(input())

    for _ in range(number_of_cloth):
        cloth, category = input().split()

        if category not in closet:
            closet[category] = []
            closet[category].append(cloth)

        else:
            closet[category].append(cloth)

    # 전체 경우의 수 : (전체 개수) + 아예 안 고르는 경우의 수
    all_clothes = [len(value) + 1 for _, value in closet.items()]

    # 모든 조합을 다 구하는 코드
    '''
    import itertools

    all_clothes = [value for key, value in closet.items()]

    combinations = list(itertools.product(*all_clothes))
    answer = set()

    for subset in combinations:
        for k in range(len(subset) + 1):
            for combination in itertools.combinations(subset, k):
                answer.add(combination)
    '''

    # 실제로는 그냥 간단한 경우의 수 문제라서, 산수로 풀 수 있다.
    # -1은 공집합 제외하기 때문에
    answer = functools.reduce(lambda x, y: x * y, all_clothes) - 1
    print(answer)

    closet = {}
