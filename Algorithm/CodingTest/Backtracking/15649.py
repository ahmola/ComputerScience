from itertools import combinations, permutations

n, m = map(int, input().split(" "))
sequence = []

for comb in combinations(range(1, n+1),m):
    for per in permutations(comb):
        sequence.append(list(per))

sequence.sort()
for s in sequence: print(*s)