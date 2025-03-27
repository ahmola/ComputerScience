import sys
# 가짓수가 여러 개인 경우에는 해당 가짓수 별로 나누어서 각 케이스를 계산한 뒤에 조건에 맞게 값을 선별한다.
def dp(rgb, memo, cost, n):
    if cost[n] != 0:
        return cost[n]

    memo[n][0] = min(memo[n-1][1]+rgb[n][0], memo[n-1][2]+rgb[n][0])
    memo[n][1] = min(memo[n-1][0]+rgb[n][1], memo[n-1][2]+rgb[n][1])
    memo[n][2] = min(memo[n-1][0]+rgb[n][2], memo[n-1][1]+rgb[n][2])
    cost[n] = min(memo[n])

    return cost[n]

n = int(sys.stdin.readline().strip())
rgb = [[] for _ in range(1001)]
for i in range(1, n+1):
    a,b,c = map(int, sys.stdin.readline().split())
    rgb[i] = [a,b,c]

memo = [[0, 0, 0] for _ in range(1001)]
cost = [0]*1001
memo[1][0] = rgb[1][0]
memo[1][1] = rgb[1][1]
memo[1][2] = rgb[1][2]
cost[1] = min(memo[1])

for i in range(2, n+1):
    dp(rgb, memo, cost, i)

print(cost[n])