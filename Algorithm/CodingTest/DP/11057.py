import sys
sys.setrecursionlimit(10**6)

def dp(n):
    memo = [[0] * 10 for _ in range(n + 1)]
    for i in range(10):
        memo[1][i] = 1
    for i in range(2, n+1):
        for j in range(10):
            memo[i][j] = sum(memo[i-1][:j+1]) % 10007

    return sum(memo[n])%10007

n = int(sys.stdin.readline().strip())
print(dp(n))