dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]
# 메모이제이션을 통해 전부 기록하여 기억해두는게 더 빠르다
for i in range(2, 41) :
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1] 

t = int(input())
result = []
for _ in range(t) :
    testcase = int(input())
    result.append(dp[testcase])

for r in result : print(f"{r[0]} {r[1]}")