from itertools import combinations

n = int(input())
grid = []

for l in range(1, 11):
    for comb in combinations(range(10), l):
        num = int("".join(map(str, sorted(comb, reverse=True))))
        grid.append(num)

grid.sort()
print(grid[n] if n < len(grid) else -1)