import sys
from itertools import product

def solution(numbers, target):
    count = 0
    for pro in product(["+", "-"], repeat = len(numbers)):
        sum = 0
        for i in range(len(numbers)):
            if pro[i] == "+":
                sum += numbers[i]
            else:
                sum -= numbers[i]
        if sum == target:
            count += 1
    return count

target = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
print(solution(numbers, target))