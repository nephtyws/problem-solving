# https://www.facebook.com/hackercup/problem/2426282194266338/


# Constraints
# 1. Alpha frog가 leap하기 위해서는 반드시 1마리 이상의 Beta frog를 뛰어넘어야 한다.
# 2. Alpha frog가 Beta frog와 붙어있을 때만 leap가 가능하다.
# e.g.) AB. (O) A.B. (X)
# 3. Beta frog는 좌우로 움직일 수 있다.

if __name__ == "__main__":
    number_of_test_case = int(input())

    inputs = []

    for _ in range(number_of_test_case):
        inputs.append(input())

    for i, case in enumerate(inputs):
        # 1. Beta frog가 없을 때 : 도약 불가능
        if 'B' not in case:
            print(f"Case #{i + 1}: N")

        # 2. 빈 땅이 없을 때 : 도약 불가능
        elif '.' not in case:
            print(f"Case #{i + 1}: N")

        elif case.count('B') >= case.count('.'):
            print(f"Case #{i + 1}: Y")

        # 다른 점 : A가 뒤로 갈 수도 있다!
        elif case.count('B') >= 2:
            print(f"Case #{i + 1}: Y")

        else:
            print(f"Case #{i + 1}: N")
