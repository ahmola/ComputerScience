from itertools import combinations


n, m = map(int, input().split(" "))

cards = list(map(int, input().split(" ")))

max_value = 0
for comb in combinations(cards, 3):
    if max_value <= sum(comb) <= m :
        max_value = sum(comb)

print(max_value)