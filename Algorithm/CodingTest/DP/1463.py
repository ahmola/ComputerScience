import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
# n이라고 설정하지말고 그냥 범위보다 1큰수로 설정해야된다
memo = [0]*100001
memo[2], memo[3] = 1,1

for i in range(4, n+1):
    if i % 6 == 0:
        memo[i] = min(memo[i-1], memo[i//2], memo[i//3]) +1
    elif i % 2 == 0:
        memo[i] = min(memo[i-1], memo[i//2]) + 1
    elif i % 3 == 0:
        memo[i] = min(memo[i-1], memo[i//3]) + 1
    else:
        memo[i] = memo[i-1] + 1
print(memo[n])