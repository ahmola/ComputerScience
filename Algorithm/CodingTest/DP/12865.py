import sys

n, k = map(int, sys.stdin.readline().split())
goods = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

memo = [0]*(k+1)
# knapsack
# dp를 활용하여 k의 범위를 넘어가지 않는 한도 내에서 값을 탐색하여 최댓값을 구함
for weight, value in goods:
    for i in range(k, weight-1, -1):
        memo[i] = max(memo[i], memo[i-weight]+value)

print(max(memo))