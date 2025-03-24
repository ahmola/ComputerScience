import sys

n, m, k = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))
friend = list(set(map(int, sys.stdin.readline().split())) for _ in range(m))
friendo = []

# 교집합이 있는 집합을 묶어서 하나의 집합으로 만듦

# 교집합 중에서 가장 적은 비용이 드는 것을 골라서 총 비용을 계산
money = 0
for fri in friendo:
    min_money = float("inf")
    for f in fri:
        min_money = min(min_money, cost[f-1])
    money += min_money

# 총 비용이 가진 돈보다 적은지 판별
if money > k:
    print("Oh no")
else:
    print(money)