# 앞으로는 무조건 입력최댓값+1로 하는게 맞겠다.
import sys

def dp(n):
    if n <= 2:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = dp(n-1) + dp(n-2)
    return memo[n]

n = int(sys.stdin.readline().strip())
memo = [0]*1001
memo[1] = 1
memo[2] = 2
# 2*3일 때, 2*1과 2*2로 나눠서 생각할 수 있다.
# 그 다음 경우도 마찬가지, 2*4를 2*3과 2*1로 나눠서 생각할 수 잇다.
print(dp(n)%10007)