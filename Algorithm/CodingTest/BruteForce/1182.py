from itertools import combinations

n, s = map(int, input().split(" "))

numbers = list(map(int, input().split(" ")))
count = 0

for i in range(1, len(numbers)+1):
    for comb in combinations(numbers, i):
        if sum(comb) == s:
            count += 1

print(count)