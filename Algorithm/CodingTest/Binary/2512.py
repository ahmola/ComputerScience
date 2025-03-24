import sys

n = int(sys.stdin.readline().strip())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())

left, right = 0, max(budget)
result = 0

while left <= right:
    cost = (left+right)//2
    cost_sum = sum(min(b, cost) for b in budget)

    if cost_sum <= m:
        result = cost
        left = cost+1
    else:
        right = cost-1

print(result)