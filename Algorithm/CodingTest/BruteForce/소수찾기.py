from itertools import permutations

def solution(numbers):
    numbers = [num for num in numbers]
    cand = set()
    for i in range(1, len(numbers)+1):
        for per in permutations(numbers, i):
            cand.add(int("".join(per)))
    max_number = max(cand)

    sieve = [False, False] + [True]*(max_number-1)
    # 에라토스테네스의 체
    # 2부터 구하려는 숫자들에서 가장 큰 수의 루트값까지 반복하면서 해당 수를 약수로 가지는 수를 걸러낸다.
    # 가령, 2는 소수이나 2를 약수로 하는 수들은 소수가 아니므로 이를 걸러낸다.
    for i in range(2, int(max_number**0.5)+1):
        if sieve[i]:
            for j in range(i*i, max_number+1, i):
                sieve[j] = False

    return sum(1 for c in cand if sieve[c])