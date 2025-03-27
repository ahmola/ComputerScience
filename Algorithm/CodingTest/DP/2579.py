import sys

def dp(stairs, n):
    if memo[n] != 0:
        return memo[n]

    memo[n] = max(dp(stairs,n-2)+stairs[n], dp(stairs, n-3)+stairs[n-1]+stairs[n])
    return memo[n]

n = int(sys.stdin.readline().strip())
stairs = [0]*301
for i in range(1, n+1):
    stairs[i] = int(sys.stdin.readline().strip())
memo = [0]*301
memo[1] = stairs[1]
memo[2] = stairs[1] + stairs[2]
memo[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

print(dp(stairs, n))