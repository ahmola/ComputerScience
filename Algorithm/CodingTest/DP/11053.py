import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [1]*n

# 각 원소를 수열의 끝이라고 생각하고 앞에서 작은 원소의 수가 순차적으로 몇 개 있는지 셈
for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))